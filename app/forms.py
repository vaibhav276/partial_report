from flask.ext.wtf import Form, validators
from wtforms import StringField, PasswordField, BooleanField, SelectField, \
        TextField, RadioField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=1,max=20)])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(max=20)])
    remember_me = BooleanField('Remember me', default=False)

class RegisterForm(Form):
    gender_ = [('Male','Male'), ('Female','Female')]
    first_name = StringField('First Name',
                             validators=[DataRequired(), Length(min=1,max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(),
                                                     Length(min=1,max=20)])
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=1,max=20)])
    age = IntegerField('Age', validators=[DataRequired(),
                                         NumberRange(min=18,max=100)])
    gender = RadioField('Gender', choices=gender_, validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=6,max=20)])

class ExperimentForm(Form):
    data_type_ = [('1', 'Alphabets'), ('2', 'Numbers')]
    matrix_sizes_ = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')]

    num_trials = IntegerField('Number of trials per segment (there are 4 \
                             segments)', validators=[DataRequired(),
                                                     NumberRange(min=1,max=20)])
    matrix_size = SelectField('Matrix Size', choices=matrix_sizes_,
                              validators=[DataRequired()])
    data_type = SelectField('Data Type', choices = data_type_,
                            validators=[DataRequired()])

class ExperimentTrialForm(Form):
    experiment_id = TextField('Experiment ID')
    experiment_trials_count = TextField('Experiment trials count')
    experiment_training = TextField('Experiment trials count')
    trial_id = StringField('Trial ID')
    trial_matrix = TextField('Matrix')
    trial_matrix_size = TextField('Matrix Size')
    trial_matrix_data_type = TextField('Data type')
    trial_cue_row = TextField('Cue Row')
    trial_duration = TextField('Duration')
    trial_response = StringField('Response', validators=[DataRequired(),
                                                         Length(max=10)])
    trial_sequence_num = TextField('Sequence number')
