from ccms import db


class Teacher(db.Model):
    __tablename__ = 't_teacher'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    no = db.Column(db.String(20), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(20))
    birthday = db.Column(db.Date)
    id_number = db.Column(db.String(20))

