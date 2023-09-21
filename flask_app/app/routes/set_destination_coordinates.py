from app import app
from flask import Flask, request, jsonify
from app.services.services_set_destination_coordinates import services_set_destination_coordinates
@app.route('/set_destination_coordinates', methods=['GET','POST'])
def set_destination_coordinates():
    try:
        if request.method == 'GET':
            device_id = request.args.get('device_id')
            destination_longitude = request.args.get('destination_longitude')
            destination_latitude = request.args.get('destination_latitude')
        else:
            device_id = request.form.get('device_id')
            destination_longitude = request.form.get('destination_longitude')
            destination_latitude = request.form.get('destination_latitude')
        return services_set_destination_coordinates(device_id,destination_latitude,destination_longitude)
    except Exception as e:
        return jsonify({"error": str(e)})