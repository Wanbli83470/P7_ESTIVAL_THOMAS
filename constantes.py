# -*- coding: utf-8 -*-
import random as r

MY_NAME = "ESTIVAL Thomas"
TITLE = "GrandPyBot"
CATCH_PHRASE = "Soufflez à l'oreille de GranpaPython... il vous offrira ses secrets..."

# Choix de 3 phrases aléatoire pour afficher l'adresse
GRANDPY1 = ["Bien sûr mon poussin : ", "Si mes souvenirs sont bons... : ", "Je me rappelle l'avoir visité dans cette rue :"]
RANDOM1 = r.choice(GRANDPY1)

# Choix de 3 phrases aléatoire pour afficher le texte avant wikipedia.
GRANDPY2 = ["Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? ", " A l'époque on jouait aux billes avec mes copains, ce quartier : "]
RANDOM2 = r.choice(GRANDPY2)

DICO_LINK = {
	"facebook" : "https://www.facebook.com/thomas.estival.9",
	"linkedin" : "https://www.linkedin.com/in/thomas-estival-384424152/",
	"git_hub" : "https://github.com/Wanbli83470",
}

DICO_IMAGE = {
	"image_facebook" : "static/fb.svg",
	"image_linkedin" : "static/linkedin.svg",
	"image_github" : "static/git_hub.svg",
	"logo" : "static/loupe.svg",
	"gif_search" : "static/anim3.gif",
}

def RANDOM():
	return r.choice(GRANDPY1)

def RANDOM2():
	return r.choice(GRANDPY2)