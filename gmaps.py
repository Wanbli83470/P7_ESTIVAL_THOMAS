"""Import the request module as 'search' """
import requests as search
from password import KEY_GMAPS
import json


class RequestMap:

    def __init__(self, words = "versaille", json_object = dict, http_get = str):
        self.words = words
        self.http_get = search.get('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(self.words, KEY_GMAPS))
        self.json_object = self.http_get.json()

    def response(self):
        return self.http_get.status_code

    def get_adress(self):
        """The address method retrieves a formatted and readable address"""
        adress = self.json_object["results"][0]["formatted_address"]
        return adress

    def get_location(self):
        """We retrieve the geographical coordinates"""
        lat = self.json_object["results"][0]["geometry"]["location"]["lat"]
        lng = self.json_object["results"][0]["geometry"]["location"]["lng"]
        location = (lat, lng)
        return location