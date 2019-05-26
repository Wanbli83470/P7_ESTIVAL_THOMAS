"""Import the request module as 'search'"""
"""Import the json module to extract information from our query"""
import requests as r
import json

class RequestWiki:

    """Class constructor to set the coordinates and the number of sentences of the summary"""

    def __init__(self, lat=43.700000, lng=7.250000, nb_phrase=2):
        self.lat = lat
        self.lng = lng
        self.nb_phrase = nb_phrase

    def geo_search(self):
        """Initialization of the url with geosearch to recover data json"""
        url = "https://fr.wikipedia.org/w/api.php?action=query&list=geosearch&gscoord={}|{}&gsradius=10000&gslimit=10&format=json".format(self.lat, self.lng)
        self.geo = r.get(url)
        status = self.geo.status_code
        print(status)
        return status

    def get_adress(self):
        geo_json = self.geo.json()

        # On recupère l'Id de la page'
        id_geo_json = geo_json['query']['geosearch'][0]['pageid']

        # On récupère le titre
        title_geo_json = geo_json['query']['geosearch'][0]['title']

        # On formate la chaine de caractère pour l'intégrer dans la requête API
        title_geo_json = title_geo_json.replace(" ", "%20")

        return title_geo_json, id_geo_json

    def resume(self, url, id_page):
        resume_json = r.get("https://fr.wikipedia.org/w/api.php?action=query&titles={}&prop=extracts&exsentences=2&format=json&explaintext".format(url))
        resume_json = resume_json.json()
        resume_json = resume_json['query']['pages'][str(id_page)]['extract']

        return resume_json

test = RequestWiki()
test.geo_search()
info_api = test.get_adress()

print(info_api)
test.resume(url = info_api[0], id_page = info_api[1])