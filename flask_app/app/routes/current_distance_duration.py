  
from app import app
from app.services.services_current_distance_duration import services_current_distance_duration
from flask import Flask, request, jsonify
@app.route('/current_distance_duration')
def current_distance_duration():
    try:
        if  request.method == 'GET':
            device_id = request.args.get('device_id')
        else:
            device_id=request.form.get('device_id')
        
        return services_current_distance_duration(device_id)
    except Exception as e:
        print("error")
        return jsonify({"error": str(e)})