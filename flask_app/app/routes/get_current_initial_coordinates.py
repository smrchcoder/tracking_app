from app import app
from flask import Flask,request,jsonify
from app.services.services_current_initial_coordinates import services_get_current_initial_coordinates
@app.route('/get_current_initial_coordinates', methods=['GET'])
def get_current_initial_coordinates():
    try:
        device_id = request.args.get('device_id')
        return services_get_current_initial_coordinates(device_id)
    except Exception as e:
        return jsonify({"error": str(e)})