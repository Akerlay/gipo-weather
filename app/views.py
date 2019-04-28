from flask import render_template, flash, redirect
from app import app
from app.forms import CityForm
from app.adapters import Adapter, YandexWeatherAdapter


weather_api: Adapter = YandexWeatherAdapter()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CityForm()
    city = form.city.data
    if city:
        real_title, forecast = weather_api.get_forecast(city)
        return render_template('weather.html',
                               title=real_title,
                               form=form,
                               city=real_title,
                               forecast=forecast)

    return render_template('base.html',
                           title='Home',
                           form=form
                           )
