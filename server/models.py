from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __init__(self, email, password, name):
        # self.id = id
        self.email = email
        self.password = password
        self.name = name

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hostname = db.Column(db.String(100))
    ip = db.Column(db.String(100))
    cpu_min = db.Column(db.Integer)
    mem_min = db.Column(db.Integer)
    hard_min = db.Column(db.Integer)
    cpu_max = db.Column(db.Integer)
    mem_max = db.Column(db.Integer)
    hard_max = db.Column(db.Integer)
    data_fresh = db.Column(db.String(100))

    def __init__(self, hostname, ip, cpu_min, mem_min, hard_min, cpu_max, mem_max, hard_max, data_fresh):
        self.hostname = hostname
        self.ip = ip
        self.cpu_min = cpu_min
        self.mem_min = mem_min
        self.hard_min = hard_min
        self.cpu_max = cpu_max
        self.mem_max = mem_max
        self.hard_max = hard_max
        self.data_fresh = data_fresh

    def get_ip(self):
        return self.ip