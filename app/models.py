from app import db
import uuid
from datetime import datetime

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

    def __repr__(self):
        return '<User %r>' % (self.username)
