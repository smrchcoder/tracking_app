from app.repo.create_cursor import connect_db
from flask import jsonify

def services_get_current_initial_coordinates(device_id):
    try:
        conn, cursor = connect_db()  # Get both connection and cursor

        cursor.execute("SELECT latitude, longitude FROM InitialCoordinates WHERE device_id = %s", (device_id,))
        data = cursor.fetchall()

        conn.close()  # Close both cursor and connection
        cursor.close()

        if not data:
            return jsonify({'message': "Could not find device", 'device_id': device_id})
        
        lat = data[0][0]
        lon = data[0][1]

        return jsonify({'latitude': lat, 'longitude': lon})
    except Exception as e:
        return jsonify({"error": str(e)})
