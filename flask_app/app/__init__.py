from flask import Flask
from flask_cors import CORS
import googlemaps
app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.py')
from app.routes import current_distance_duration,get_current_destination,get_current_initial_coordinates,insert_data_random,insert_data,set_destination_coordinates,set_initial_coordinates,set_initial_coordinates


