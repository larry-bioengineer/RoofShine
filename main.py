# Larry TO
# Created on: 8/1/2020
# A web app for Solis's project RoofShine 

from flask import Flask
from flask_googlemaps import GoogleMaps
import config

app = Flask(__name__)

@app.route("/")
def home():
	return render_templates("home.html")


if __name__ == "__main__":
	app.run(debug=True)