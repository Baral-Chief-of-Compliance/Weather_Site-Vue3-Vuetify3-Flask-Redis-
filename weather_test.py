import requests, json, redis, time
import os
from dotenv import load_dotenv


load_dotenv()

token = os.getenv('WEATHER_API_YANDEX')


def get_inf_weather(long, lat, name):

    r = requests.get(f'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={long}&extra=true', headers={"X-Yandex-API-Key": token})

    red = redis.Redis(host='localhost', port=6379, db=3)

    weather = {}

    data_from_yandex = r.json()

    for key in data_from_yandex:
        if (key == "fact"):
            weather = data_from_yandex[key]

    json_weather = json.dumps(weather)

    red.set(name, json_weather)
    print(time.strftime("\n\n%A, %d. %B %Y %I:%M:%S %p") + str(": weather date enter to redis"))


def get_weather_long_lat(long, lat):

    r = requests.get(f'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={long}&extra=true', headers={"X-Yandex-API-Key": token})

    weather = {}

    data_from_yandex = r.json()

    for key in data_from_yandex:
        if (key == "fact"):
            weather = data_from_yandex[key]


    print('\n\n'+f'information about {long} {lat} get from Yandex_API')

    return weather