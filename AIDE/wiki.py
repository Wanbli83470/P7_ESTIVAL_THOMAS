"""Import the request module as 'search'"""
"""Import the json module to extract information from our query"""
import requests as r
import json

class RequestWiki:

    """Class constructor to set the coordinates and the number of sentences of the summary"""

    def __init__(self, lat=48.8534, lng=2.3488, nb_phrase=2):
        self.lat = lat
        self.lng = lng
        self.nb_phrase = nb_phrase

    def geo_search(self):
        """Initialization of the url with geosearch to recover data json"""
        url = "https://fr.wikipedia.org/w/api.php?action=query&list=geosearch&gscoord={}|{}&gsradius=10000&gslimit=10&format=json".format(self.lat, self.lng)
        self.geo = r.get(url)
        print(self.geo)

    def get_adress(self):
        geo_json = self.geo.json()
        geo_json = geo_json['query']['geosearch'][0]['title']
        print(geo_json)

    def resume(self):
        resume_json = r.get("https://fr.wikipedia.org/w/api.php?action=query&titles=Boulevard%20Michelet%20(Marseille)&prop=extracts&exsentences=3&format=json&explaintext")
        resume_json = resume_json.json()
        resume_json = resume_json['query']['pages'][1]

        print(resume_json)

test = RequestWiki()
test.geo_search()
test.get_adress()
test.resume()
