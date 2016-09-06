from flask import render_template, flash, redirect, request
from app import app, db, models
from .forms import LoginForm, RegisterForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
            title = 'Index'
            )

@app.route('/login', methods=['GET', 'POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
       flash('Login requested for username = %s, remember_me = %s' %
               (form.username.data, str(form.remember_me.data))
               )
       print 'redirecting'
       return redirect('/partial_report/index')
   return render_template('login.html',
           title = 'Sign in',
           form = form
           )

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(username = str(form.username.data)).first()
        if user is not None:
            flash('username "%s" already exists. Try another one.' % str(form.username.data))
            return redirect('/register')
        else:
            user = models.User(username = str(form.username.data),
                    first_name = str(form.first_name.data),
                    last_name = str(form.last_name.data),
                    age = str(form.age.data),
                    gender = str(form.gender.data),
                    password = str(form.password.data))
            db.session.add(user)
            db.session.commit()
            flash('Registration successful for username ' + form.username.data)
            return redirect('/index')
    return render_template('register.html',
            title = 'Register',
            form = form,
            )
