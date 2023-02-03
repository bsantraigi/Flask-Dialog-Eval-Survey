# model.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class Annotator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_token = db.Column(db.String(6), unique=True, nullable=False)

    def __repr__(self):
        return f'<Annotator id={self.id} id_token={self.id_token}>'

class Dialog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dialog_context = db.Column(db.String(200), nullable=False)
    response_a_model = db.Column(db.String(100), nullable=False)
    response_a = db.Column(db.String(100), nullable=False)
    response_b_model = db.Column(db.String(100), nullable=False)
    response_b = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Dialog id={self.id} dialog_context={self.dialog_context} response_a_model={self.response_a_model} response_a={self.response_a} response_b_model={self.response_b_model} response_b={self.response_b}>'

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dialog_id = db.Column(db.Integer, db.ForeignKey('dialog.id'), nullable=False)
    annotator_id = db.Column(db.Integer, db.ForeignKey('annotator.id'), nullable=False)
    coherence_a = db.Column(db.String(10), nullable=False)
    coherence_b = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<Rating id={self.id} dialog_id={self.dialog_id} annotator_id={self.annotator_id} coherence_a={self.coherence_a} coherence_b={self.coherence_b}>'

