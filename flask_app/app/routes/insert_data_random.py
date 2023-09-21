from flask import Flask, request, jsonify
import time
import requests
from app import app
import random
from app.services.services_insert_data import services_insert_data
@app.route('/insert_data_random', methods=['POST', 'GET'])
def insert_data_random():
    try:
        if request.method == 'POST':
            device_id = request.form.get('device_id')
            timestamp = request.form.get('timestamp')
            latitude = request.form.get('latitude')
            longitude = request.form.get('longitude')
        else:
            device_id = request.args.get('device_id')
            timestamp = request.args.get('timestamp')
            latitude = request.args.get('latitude')
            longitude = request.args.get('longitude')

        return (services_insert_data(device_id,latitude,longitude,timestamp))

    except Exception as e:
        return jsonify({"error": str(e)})
