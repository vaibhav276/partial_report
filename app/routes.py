from flask import render_template, flash, redirect, request, url_for, g, \
session
from app import app, db, models, lm
from .forms import LoginForm, RegisterForm
from utils import encrypt_password, verify_password
from flask.ext.login import login_user, logout_user, current_user, \
login_required

@lm.user_loader
def load_user(id):
    return models.User.query.get(id)

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
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
            flash('username "%s" already exists. Try another one.' \
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
