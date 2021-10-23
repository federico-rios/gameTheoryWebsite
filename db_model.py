from main import db

class Matrix(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    description = db.Column(db.String(1000))
    # matrix_object
    rounds = db.relationship("Round", backref="game")


class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round_num = db.Column(db.Integer)
    matrix_id = db.Column(db.Integer, db.ForeignKey("matrix.id"))