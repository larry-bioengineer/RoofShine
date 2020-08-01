# Larry TO
# Created on: 8/1/2020
# A web app for Solis's project RoofShine 

from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

import config

app = Flask(__name__)

# Initialize map
GoogleMaps(app, key = config.google_api)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/map")
def map_unbounded():
    map = Map(
    	identifier="view-side",
        lat= 22.243434,
        lng= 114.147204,
        markers=[(22.243434, 114.147204)]
    )
    return render_template('map.html', map=map)

if __name__ == "__main__":
	app.run(debug=True)