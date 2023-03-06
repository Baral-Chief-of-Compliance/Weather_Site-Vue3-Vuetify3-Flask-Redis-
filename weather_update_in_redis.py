import redis
from weather_test import get_inf_weather
import geo


def update_redis():
    r = redis.StrictRedis(host='localhost', port=6379, db=3)

    keys = r.keys()

    for k in keys:

        long = geo.get_longitude(k.decode('utf-8'))
        lat = geo.get_latitude(k.decode('utf-8'))

        name_of_key = k.decode('utf-8')

        get_inf_weather(long, lat, name_of_key)

        print(f'date about {name_of_key} update')

    print('\n\ndate in redis update')