from geopy import Yandex
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('GEO_API_YANDEX')

def get_longitude(place):
    location = Yandex(api_key=token).geocode(place)
    return location.longitude


def get_latitude(place):
    location = Yandex(api_key=token).geocode(place)
    return location.latitude