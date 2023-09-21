from app.repo.create_cursor import connect_db
from flask import Flask, request, jsonify
def services_set_destination_coordinates(device_id, destination_latitude, destination_longitude):
    try:
        conn, cursor = connect_db() 
        cursor.execute("UPDATE InitialCoordinates SET destination_longitude = %s, destination_latitude = %s WHERE device_id = %s",
                       (destination_longitude, destination_latitude, device_id))
        conn.commit()
        conn.close()

        return jsonify({"message": "Destination coordinates set successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})