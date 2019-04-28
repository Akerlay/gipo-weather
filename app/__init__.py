from flask import Flask
import json

REQUIRED_CONFIG_FIELDS = ['CSRF_ENABLED', 'SECRET_KEY', 'YANDEX_WEATHER_KEY', 'YANDEX_GEOCODER_KEY']
CONFIG_PATH = 'config.json'


config = json.load(open(CONFIG_PATH, 'r'))

for field in REQUIRED_CONFIG_FIELDS:
    if field not in config:
        config[field] = input(field + ': ')

json.dump(config, open(CONFIG_PATH, 'w'))

app = Flask(__name__)
app.config.from_mapping(config)

from app import views
