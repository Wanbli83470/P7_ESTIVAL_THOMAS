"""Import the request module as 'search'"""
"""Import the json module to extract information from our query"""
import requests as r
import json

class RequestWiki:
    def __init__(self, lat=43.2701, lng=5.3925, nb_phrase=2):
        self.lat = lat
        self.lng = lng
        self.nb_phrase = nb_phrase

    def geo_search(self):
        url = "https://fr.wikipedia.org/w/api.php?action=query&list=geosearch&gscoord={}|{}&gsradius=10000&gslimit=10&format=json".format(self.lat, self.lng)
        print(url)
        self.geo = r.get(url)
        print(self.geo)


    def get_adress(self):
        geo_json = self.geo.json()



test = RequestWiki()
test.geo_search()
test.get_adress()
