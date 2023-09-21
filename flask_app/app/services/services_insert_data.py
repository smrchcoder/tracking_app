from app.repo.create_cursor import connect_db
from flask import Flask, request, jsonify
def services_insert_data(device_id,latitude,longitude,timestamp):
    try:
        conn, cursor = connect_db() 
        cursor.execute("Select device_id from InitialCoordinates where device_id=%s",(device_id,))
        data=cursor.fetchall()
        #if the device id does not exist
        if not data:
            return jsonify({'message':'device id does not exist','device_id':device_id})
        else:
            cursor.execute("UPDATE InitialCoordinates SET longitude = %s, latitude = %s WHERE device_id = %s",
                            (longitude, latitude, device_id))
            cursor.execute("INSERT INTO GPS (device_id, timestamp, longitude, latitude) VALUES (%s, %s, %s, %s)",
                           (device_id, timestamp, longitude, latitude))
        # Insert the new data
        conn.commit()
        conn.close()

        return jsonify({"message": "Data inserted successfully and Initial coordinates updated"})
    except Exception as e:
        return jsonify({"error": str(e)})