from app.services.services_insert_data import services_insert_data
from app import app
from flask import Flask, request, jsonify
@app.route('/insert_data', methods=['GET','POST'])
def insert_data():
    try:
        if request.method == 'POST':
            device_id = request.form.get('device_id')
            timestamp = request.form.get('timestamp')
            longitude = request.form.get('longitude')
            latitude = request.form.get('latitude')
            
        else:
            device_id = request.args.get('device_id')
            timestamp = request.args.get('timestamp')
            longitude = request.args.get('longitude')
            latitude = request.args.get('latitude')
        
        return services_insert_data(device_id,latitude,longitude,timestamp)
    except Exception as e:
        print("Error inserting device")
        return jsonify({"error": str(e)})