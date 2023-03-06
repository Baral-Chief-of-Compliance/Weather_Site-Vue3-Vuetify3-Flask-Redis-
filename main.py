from flask import Flask, jsonify, request
import json, redis,  atexit
from flask_cors import CORS
from weather_test import get_inf_weather, get_weather_long_lat
import geo
from weather_update_in_redis import update_redis
from apscheduler.schedulers.background import BackgroundScheduler


'''REDIS_START'''

r = redis.Redis(host='localhost', port=6379, db=3)

'''REDIS_END'''

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(update_redis, "interval", seconds=60*60)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)


@app.route('/weather/api/v1.0/place', methods=['POST'])
def check_place():
    if request.method == 'POST':

        place = {
            'name': request.json['name']
        }

        print(place)

        if r.get(place['name']):
            return jsonify(json.loads(r.get(place['name'])))

        else:

            long = geo.get_longitude(place['name'])
            lat = geo.get_latitude(place['name'])

            get_inf_weather(long, lat, place['name'])

            return jsonify(json.loads(r.get(place['name'])))


@app.route('/weather/api/v1.0/long_lat', methods=['POST'])
def check_long_lat():

    if request.method == 'POST':

        place = {
            'long': request.json['long'],
            'lat': request.json['lat']
        }

        return jsonify(get_weather_long_lat(place['long'], place['lat']))


if __name__ == '__main__':
    app.run(debug=True)
