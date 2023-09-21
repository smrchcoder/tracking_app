from app.repo.create_cursor import connect_db
from flask import  jsonify
import random
def services_insert_random(device_id, timestamp):
    try:
        min_latitude = -90.0  # Minimum latitude
        max_latitude = 90.0   # Maximum latitude
        min_longitude = -180.0  # Minimum longitude
        max_longitude = 180.0   # Maximum longitude
        latitude = round(random.uniform(min_latitude, max_latitude), 6)
        longitude = round(random.uniform(min_longitude, max_longitude), 6)

        conn, cursor = connect_db() 
        cursor.execute("SELECT device_id FROM InitialCoordinates WHERE device_id = %s", (device_id,))
        data = cursor.fetchall()
        if not data:
            return jsonify({'message': 'Device not found', 'device_id': device_id})
        else:
            cursor.execute("UPDATE InitialCoordinates SET longitude = %s, latitude = %s WHERE device_id = %s",
                            (longitude, latitude, device_id))
            cursor.execute("INSERT INTO GPS (device_id, timestamp, longitude, latitude) VALUES (%s, %s, %s, %s)",
                           (device_id, timestamp, longitude, latitude))

        conn.commit()
        conn.close()

        print(f"Data inserted successfully - Latitude: {latitude}, Longitude: {longitude}")
    except Exception as e:
        print(f"Error: {str(e)}")

