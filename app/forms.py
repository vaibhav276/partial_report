from flask.ext.wtf import Form, validators
from wtforms import StringField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me', default=False)

class RegisterForm(Form):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class ExperimentForm(Form):
    data_type_ = [(1, 'Alphabets'), (2, 'Numbers')]
    presets_ = [(1, 'Preset 1')]

    preset = SelectField('Preset', choices=presets_,
                         validators=[DataRequired()])
    num_trials = StringField('Number of trials per segment (there are 4 \
                             segments)', validators=[DataRequired()])
    matrix_size = StringField('Matrix Size', validators=[DataRequired()])
    data_type = SelectField('Data Type', choices = data_type_,
                            validators=[DataRequired()])
