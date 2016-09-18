from app import db
import uuid
from datetime import datetime
from sqlalchemy import func
import random

class User(db.Model):
    __tablename__ = 'pr_user'

    id = db.Column('id', db.String(64), primary_key=True, default=uuid.uuid4())
    username = db.Column('username', db.String(64), index=True, unique=True)
    first_name = db.Column('first_name', db.String(64), index=False, unique=False)
    last_name = db.Column('last_name', db.String(64), index=False, unique=False)
    age = db.Column('age', db.Integer(), index=False, unique=False)
    gender = db.Column('gender', db.String(10), index=False, unique=False)
    password = db.Column('password', db.String(1024), index=False, unique=False)
    creation_date = db.Column('creation_date', db.Date, default=datetime.utcnow)

    experiments = db.relationship('Experiment', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.username)

    # Functions for LoginManager
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

class Experiment(db.Model):
    __tablename__ = 'pr_experiment'

    durations_ = [20, 100, 300, 1000]

    id = db.Column('id', db.String(64), primary_key=True, default=uuid.uuid4())
    user_id = db.Column('user_id', db.String(64), db.ForeignKey('pr_user.id') )
    trials_completed = db.Column('trials_completed', db.Integer(), default=0)
    creation_date = db.Column('creation_date', db.DateTime(),
                              default=datetime.utcnow)
    training = db.Column('training', db.Boolean(), default=False)

    trials = db.relationship('Trial', backref='experiment', lazy='dynamic')

    def __init__(self):
        self.id = str(uuid.uuid4())

    def __repr__(self):
        return '<Experiment %r>' % (self.id)

    def generate(self, num_trials = 15, data_type = 'alpha', matrix_size = 3):
        trials = []
        sequence_number = 1
        for m in range(len(self.durations_)):
            for n in range(num_trials):
                trial =  Trial()
                trial.experiment_id = self.id
                trial.duration = self.durations_[m]
                trial.cue_row = random.randint(1, matrix_size)
                trial.sequence_number = sequence_number
                matrix = Matrix(size = matrix_size, data_type = data_type)
                matrix.trial_id = trial.id
                matrix.data = matrix.generate()
                trials.append((trial, matrix))
                sequence_number = sequence_number + 1

        return trials


class Trial(db.Model):
    __tablename__ = 'pr_trial'

    id = db.Column('id', db.String(64), primary_key=True, default=uuid.uuid4())
    experiment_id = db.Column('experiment_id', db.String(64),
                                db.ForeignKey('pr_experiment.id'))
    sequence_number = db.Column('sequence_number', db.Integer(), default=1)
    duration = db.Column('duration', db.Integer())
    cue_row = db.Column('cue_row', db.Integer())
    response = db.Column('response', db.String(8))
    score = db.Column('score', db.Integer())

    matrix = db.relationship('Matrix', backref='trial', lazy='dynamic')

    def __init__(self):
        self.id = str(uuid.uuid4())

    def __repr__(self):
        return '<Trial - cue row %r, duration %r>' % (self.cue_row,
                                                      self.duration)

class Matrix(db.Model):
    __tablename__ = 'pr_matrix'

    alpha_chars_ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeric_chars_ = '0123456789'

    id = db.Column('id', db.String(64), primary_key=True, default=uuid.uuid4())
    trial_id = db.Column('trial_id', db.String(64), db.ForeignKey('pr_trial.id'))
    size = db.Column('size', db.Integer()) # max 5
    data_type = db.Column('data_type', db.Integer())
    data = db.Column('data', db.String(32)) # max 25 characters

    def __init__(self, size, data_type):
        self.id = str(uuid.uuid4())
        self.size = size
        self.data_type = data_type

    def __repr__(self):
        return '<Matrix %r>' % (self.data)

    def generate(self):
        str = ''
        if self.data_type == 1:
            domain = self.alpha_chars_
        else:
            domain = self.numeric_chars_
        for i in range(self.size):
            sample = random.sample(range(1, len(domain)), self.size)
            for j in sample:
                str += domain[j]
        return str

