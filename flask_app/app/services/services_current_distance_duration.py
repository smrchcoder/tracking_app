from app.repo.create_cursor import connect_db
from flask import  jsonify
from app.repo.gmaps_config import gmaps_config
def services_current_distance_duration(device_id):
    try:
        conn, cursor = connect_db() 

        # Fetch latitude and longitude from the GPS table
        cursor.execute(
            "SELECT latitude, longitude FROM InitialCoordinates WHERE device_id = %s",
            (device_id,)
        )
        gps_data = cursor.fetchone()

        if gps_data is None:
            return jsonify({"error": "Coordinates  data not found for device_id"})

        lat, lon = gps_data

        # Fetch destination latitude and longitude from the InitialCoordinates table
        cursor.execute(
            "SELECT destination_latitude, destination_longitude FROM InitialCoordinates WHERE device_id = %s",
            (device_id,)
        )
        initial_coords_data = cursor.fetchone()

        if initial_coords_data is None:
            return jsonify({"error": "Destination coordinates not found for device_id"})

        dlat, dlong = initial_coords_data

        try:
            # Use the distance_matrix function to calculate the distance and duration
            
            origin_coords = (lat, lon)
            destination_coords = (dlat, dlong)
            gmaps=gmaps_config()
            matrix = gmaps.distance_matrix(
                origin_coords, destination_coords, units="metric", mode="driving"
            )
            
            print(matrix)
            # Extract the distance value (in meters) from the response
            distance_in_meters = matrix["rows"][0]["elements"][0]["distance"]["value"]

            # Extract the duration value (in seconds) from the response
            duration_in_seconds = matrix["rows"][0]["elements"][0]["duration"]["value"]

            # Convert meters to kilometers
            distance_in_kilometers = distance_in_meters / 1000

            # Convert seconds to minutes
            duration_in_minutes = duration_in_seconds / 60

            conn.close()
            print(distance_in_kilometers,duration_in_minutes)
            return jsonify({"distance": distance_in_kilometers, "duration": duration_in_minutes})

        except Exception as e:
            print('Error')
            return jsonify({"error": str(e)})

    except Exception as e:
        return jsonify({"error": "An error occurred while calculating distance and duration"})




