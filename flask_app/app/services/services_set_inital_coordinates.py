from app.repo.create_cursor import connect_db
from flask import Flask, request, jsonify

def services_set_initial_coordinates(device_id,latitude,longitude,timestamp):
    try:
        if device_id is not None and longitude is not None and latitude is not None and timestamp is not None:
            conn, cursor = connect_db() 
            cursor.execute("SELECT device_id FROM InitialCoordinates WHERE device_id = %s", (device_id,))
            data = cursor.fetchall()
            
            if not data:
                cursor.execute("INSERT INTO InitialCoordinates (device_id, longitude, latitude) VALUES (%s, %s, %s)",
                                (device_id, longitude, latitude))
            else:
                cursor.execute("UPDATE InitialCoordinates SET longitude = %s, latitude = %s WHERE device_id = %s",
                                (longitude, latitude, device_id))
            
            cursor.execute("INSERT INTO GPS (device_id, timestamp, longitude, latitude) VALUES (%s, %s, %s, %s)",
                            (device_id, timestamp, longitude, latitude))
            
            conn.commit()
            conn.close()
            return jsonify({"message": "Coordinates successfully inserted"})
        else:
            return jsonify({"error": "Missing required parameters (device_id, longitude, latitude, timestamp)"})
    except Exception as e:
        return jsonify({"error": str(e)})