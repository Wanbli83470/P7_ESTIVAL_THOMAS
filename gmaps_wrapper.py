"""Importe the google maps wrapper"""
import googlemaps
from password import KEY_GMAPS
"""login using the API key"""
gmaps = googlemaps.Client(key=KEY_GMAPS)

class RequestMap:

    """This class retrieves a formatted address and geographic coordinates using the wrapper"""

    def __init__(self, requete, result=None):
        self.requete = requete
        self.result = gmaps.geocode(self.requete)
        self.result = self.result[0]

    def get_adress(self):
        """The address method retrieves a formatted and readable address"""
        self.adress = self.result["formatted_address"]
        return self.adress

    def get_location(self):
        """We retrieve the geographical coordinates"""
        self.geometry = self.result.get("geometry")
        self.location = self.geometry.get("location")
        return self.location