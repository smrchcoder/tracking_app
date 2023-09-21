from app import app
from flask import Flask, request, jsonify
from app.services.services_get_current_destination import services_get_current_destination
@app.route('/get_current_destination')
def get_current_destination():
    try:
        device_id=request.args.get('device_id')
        return services_get_current_destination(device_id)
        
    except Exception as e:
        return jsonify({"error": str(e)})