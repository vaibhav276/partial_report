from flask.ext.wtf import Form, validators
from wtforms import StringField, PasswordField, BooleanField, SelectField, \
        TextField
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
    data_type_ = [('1', 'Alphabets'), ('2', 'Numbers')]
    presets_ = [('1', 'Preset 1')]
    matrix_sizes_ = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')]

    preset = SelectField('Preset', choices=presets_,
                         validators=[DataRequired()])
    num_trials = StringField('Number of trials per segment (there are 4 \
                             segments)', validators=[DataRequired()])
    matrix_size = SelectField('Matrix Size', choices=matrix_sizes_,
                              validators=[DataRequired()])
    data_type = SelectField('Data Type', choices = data_type_,
                            validators=[DataRequired()])

class ExperimentTrialForm(Form):
    experiment_id = TextField('Experiment ID')
    experiement_trials_count = TextField('Experiment trials count')
    trial_id = StringField('Trial ID')
    trial_matrix = TextField('Matrix')
    trial_matrix_size = TextField('Matrix Size')
    trial_matrix_data_type = TextField('Data type')
    trial_cue_row = TextField('Cue Row')
    trial_duration = TextField('Duration')
    trial_response = StringField('Response', validators=[DataRequired()])
    trial_sequence_num = TextField('Sequence number')
