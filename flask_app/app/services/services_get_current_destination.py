from app.repo.create_cursor import connect_db
from flask import jsonify

def services_get_current_destination(device_id):
    try:
        conn, cursor = connect_db()  # Get both connection and cursor

        cursor.execute("SELECT destination_latitude, destination_longitude FROM InitialCoordinates WHERE device_id = %s", (device_id,))
        data = cursor.fetchall()

        conn.close()  # Close both cursor and connection
        cursor.close()

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})
