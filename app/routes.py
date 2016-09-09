from flask import render_template, flash, redirect, request, url_for, g, \
session
from app import app, db, models, lm
from .forms import LoginForm, RegisterForm, ExperimentForm
from utils import encrypt_password, verify_password
from flask.ext.login import login_user, logout_user, current_user, \
login_required

@lm.user_loader
def load_user(id):
    return models.User.query.get(id)

@app.before_request
def before_request():
    g.user = current_user


app.static_url_path = 'static/'

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('index.html',
                           title = 'Index',
                           user = g.user
                          )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        #flash('Login requested for username = %s, remember_me = %s' %
        #(form.username.data, str(form.remember_me.data))
        #)
        user = models.User.query.filter_by(username = \
                                           str(form.username.data)).first()
        if user is None:
            flash('username "%s" not registered. Please register' \
                  % str(form.username.data))
            return render_template('login.html',
                                   title = 'Sign in',
                                   form = form,
                                   user = g.user
                                  )
        elif verify_password(form.password.data, user.password) is False:
            flash('Invalid password')
            return render_template('login.html',
                                   title = 'Sign in',
                                   form = form,
                                   user = g.user
                                  )
        else:
            session['remember_me'] = form.remember_me.data
            login_user(user, remember = form.remember_me.data)
            return redirect(request.args.get('next') or url_for('dashboard'))

    return render_template('login.html',
                           title = 'Sign in',
                           form = form,
                           user = g.user
                          )

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(username = \
                                           str(form.username.data)).first()
        if user is not None:
            flash('Username %s already exists. Try another one.' \
                  % str(form.username.data))
            return redirect(url_for('register'))
        else:
            user = models.User(username = str(form.username.data),
                               first_name = str(form.first_name.data),
                               last_name = str(form.last_name.data),
                               age = str(form.age.data),
                               gender = str(form.gender.data),
                               password = \
                               encrypt_password(str(form.password.data)))
            db.session.add(user)
            db.session.commit()
            flash('Registration successful for username ' + form.username.data)
            return redirect(url_for('index'))
    return render_template('register.html',
                           title = 'Register',
                           form = form,
                           user = g.user
                          )

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html',
                           title = 'Dashboard',
                           user = g.user)

@app.route('/experiment', methods=['GET', 'POST'])
@login_required
def experiment():
    form = ExperimentForm()
    if form.validate_on_submit():
        experiment = models.Experiment()
        generated_tuples = experiment.generate(num_trials = int(form.num_trials.data),
                       data_type = int(form.data_type.data),
                       matrix_size = int(form.matrix_size.data)
                      )

        db.session.add(experiment)
        for (trial, matrix) in generated_tuples:
            db.session.add(trial)
            db.session.add(matrix)

        db.session.commit()

        return redirect(url_for('experiment_trial', experiment_id =
                                str(experiment.id)))

    return render_template('experiment.html',
                           title = 'New Experiment',
                           form = form,
                           user = g.user
                          )

@app.route('/experiment/<string:experiment_id>')
def experiment_trial(experiment_id):
    experiment = models.Experiment.query.filter_by( id = experiment_id
                                                  ).first()
    if experiment is None:
        flash('Experiment id %s not found. Try creating a new experiment' %
              (experiment_id)
             )
        return render_template('experiment_trial.html',
                               title = 'Experiment trial',
                               user = g.user
                              )

    if experiment.trials_completed < len(experiment.trials.all()):
        # Experiment not completed yet
        next_trial_num = experiment.trials_completed + 1
        next_trial = models.Trial.query.filter_by( experiment_id =
                                                  experiment_id,
                                                  sequence_number =
                                                  next_trial_num).first()

        if next_trial is None:
            flash('ERROR: Could not find next trial')
            return render_template('experiment_trial.html',
                                   title = 'Experiment trial',
                                   user = g.user
                                  )

        next_matrix = models.Matrix.query.filter_by( trial_id = next_trial.id
                                                   ).first()
        if next_matrix is None:
            flash('ERROR: Could not find next trial')
            return render_template('experiment_trial.html',
                                   title = 'Experiment trial',
                                   user = g.user
                                  )

    return render_template('experiment_trial.html',
                           title = 'Experiment trial',
                           user = g.user,
                           experiment_id = experiment.id,
                           trial = next_trial,
                           matrix = next_matrix
                          )

