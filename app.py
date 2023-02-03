# app.py

from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import RadioField
from wtforms import StringField, RadioField, Form, validators 
from forms import *
from flask import flash

from model import db, migrate, Annotator, Dialog, Rating
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///evaluation_survey.db'
app.config['SECRET_KEY'] = 'secret_key'

db.init_app(app)
migrate.init_app(app, db)

# class EvaluationForm(FlaskForm):
#     coherence_a = RadioField('Coherence of response A', choices=[('Yes', 'Yes'), ('Somewhat', 'Somewhat'), ('No', 'No')], validators=[validators.InputRequired()])
#     coherence_b = RadioField('Coherence of response B', choices=[('Yes', 'Yes'), ('Somewhat', 'Somewhat'), ('No', 'No')], validators=[validators.InputRequired()])

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        annotator = Annotator.query.filter_by(id_token=form.id_token.data).first()
        if annotator:
            return redirect(url_for('evaluation'))
        else:
            flash('Invalid id token. Please try again.')
    return render_template('index.html', form=form)

@app.route('/evaluation', methods=['GET', 'POST'])
def evaluation():
    form = EvaluationForm()
    annotator_id = Annotator.query.filter_by(id_token=form.id_token.data).first().id
    dialog = Dialog.query.order_by(db.func.random()).first()
    if form.validate_on_submit():
        rating = Rating(dialog_id=dialog.id, annotator_id=annotator_id, coherence_a=form.coherence_a.data, coherence_b=form.coherence_b.data)
        db.session.add(rating)
        db.session.commit()
        return redirect(url_for('submitted_results'))
    return render_template('survey.html', form=form, dialog=dialog)

@app.route('/submitted_results')
def submitted_results():
    ratings = Rating.query.all()
    return render_template('submitted_results.html', ratings=ratings)

if __name__ == '__main__':
    app.run(debug=True)

