from flask import Flask, request, jsonify
from app import app
from app.services.services_set_inital_coordinates import services_set_initial_coordinates
@app.route('/set_initial_coordinates', methods=['POST','GET'])
def set_initial_coordinates():
    try:
        if request.method == 'POST':
            device_id = request.form.get('device_id')
            longitude = request.form.get('longitude')
            latitude = request.form.get('latitude')
            timestamp = request.form.get('timestamp')
        else:
            device_id = request.args.get('device_id')
            longitude = request.args.get('longitude')
            latitude = request.args.get('latitude')
            timestamp = request.args.get('timestamp')
        return services_set_initial_coordinates(device_id, longitude, latitude, timestamp)
    
    except Exception as e:
        return jsonify({"error": str(e)})
