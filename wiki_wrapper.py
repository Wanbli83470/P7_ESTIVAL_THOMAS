"""Import the wikipedia wrapper to retrieve information about the place"""
import wikipedia
from mediawiki import MediaWiki
"""Define the French language for search"""
wikipedia.set_lang("fr")
mediawiki = MediaWiki()


class RequestWiki:

    i = 0
    extract = str()

    def __init__(self,lat=43.2701, lng=5.3925, nb_phrase = 2):
        self.lat = lat
        self.lng = lng
        self.nb_phrase = nb_phrase
        
    def geo_search(self):
        self.geo = mediawiki.geosearch(latitude=self.lat, longitude=self.lng)
        self.page = wikipedia.page(self.geo[0])

    def resume(self):
        self.resume = self.page.summary

        for l in self.resume :
            if self.i < self.nb_phrase :
                self.extract = self.extract + l
                if l == ".":
                    self.i += 1
        return '{}'.format(self.extract)

# OC = RequestWiki()
# print(OC)
# print(OC.geo_search())
# print(OC.geo)
# print(type(OC.page))
# data_wiki = OC.resume()
# print(data_wiki)
