from flask import Flask, url_for, render_template, request, jsonify
app = Flask(__name__)
from constantes import *
from gmaps import *
from parse import Parsing
from wiki import *


@app.route("/", methods=['GET', 'POST'])
def hello():
    return render_template('index.html', TITLE = TITLE, MY_NAME = MY_NAME, DICO_IMAGE = DICO_IMAGE, DICO_LINK = DICO_LINK, RANDOM1 = RANDOM1, RANDOM2 = RANDOM2)

@app.route('/response', methods = ['GET', 'POST'])
def result():
	if request.method == 'POST':
		json = request.get_json()
		# Recover user input
		question = json['question']
		print(question)

		# analyze the question with module parse
		parse = Parsing(phrase = question, nb_letter=4)
		print(parse)
		parse = parse.parser()
		print(parse)
		
		# Location with Google Maps api
		data_maps = RequestMap(parse)
		data_adress = data_maps.get_adress()
		data_location = data_maps.get_location()
		lat = data_location["lat"]
		lng = data_location["lng"]
		position = str(lat) + str(lng)
		print(position)

		# we use the coordinates to obtain wikipedia information with its API
		data_wiki = RequestWiki(lat=lat, lng=lng)
		data_wiki.geo_search()
		result_wiki = data_wiki.resume()

		# We post new answers with the random module
		random_maps = RANDOM()
		random_wiki = RANDOM2()

		parse = ""

		return jsonify(data_adress = data_adress, lat = lat, lng = lng, position = position, random_maps = random_maps, random_wiki = random_wiki, result_wiki = result_wiki)

if __name__ == '__main__':
	app.run(debug=True)
