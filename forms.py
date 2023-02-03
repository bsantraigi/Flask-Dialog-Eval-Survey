from flask_wtf import FlaskForm
from wtforms import StringField, RadioField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    id_token = StringField('id_token', validators=[InputRequired(), Length(min=6, max=6)])


class EvaluationForm(FlaskForm):
    coherence = RadioField('coherence', choices=[('Yes', 'Yes'), ('Somewhat', 'Somewhat'), ('No', 'No')],
                           validators=[InputRequired()])

