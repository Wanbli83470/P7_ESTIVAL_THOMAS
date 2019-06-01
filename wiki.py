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
        url = "https://fr.wikipedia.org/w/api.php?action=query&list=geosearch&gscoord={}|{}&gsradius=10000&gslimit=10&format=json".\
            format(self.lat, self.lng)
        self.geo = r.get(url)
        status = self.geo.status_code
        print(status)
        print(url)
        return status

    def get_adress(self):
        """Récupération de l'ID de la page et du titre pour la fonction 'resume' """
        geo_json = self.geo.json()

        # On recupère l'Id de la page'
        id_geo_json = geo_json['query']['geosearch'][0]['pageid']

        # On récupère le titre
        title_geo_json = geo_json['query']['geosearch'][0]['title']

        # On formate la chaine de caractère pour l'intégrer dans la requête API
        title_geo_json = title_geo_json.replace(" ", "%20")
        print(title_geo_json)
        return title_geo_json, id_geo_json

    def resume(self, url, id_page):
        """Configuration de l'URL d'une requête API avec les données pour extraires les phrases importantes """
        print("https://fr.wikipedia.org/w/api.php?action=query&titles={}&prop=extracts&exsentences=2&format=json&explaintext".
                            format(url))
        resume_json = r.get("https://fr.wikipedia.org/w/api.php?action=query&titles={}&prop=extracts&exsentences=2&format=json&explaintext".
                            format(url))
        resume_json = resume_json.json()
        resume_json = resume_json['query']['pages'][str(id_page)]['extract']

        return resume_json
