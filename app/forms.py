from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CityForm(FlaskForm):
    city = StringField('Город:', validators=[DataRequired()], render_kw={"placeholder": "Введите город"})
