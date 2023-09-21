import googlemaps

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'google map API Kye'

# Initialize the Google Maps client
gmaps = googlemaps.Client(key=api_key)

def calculate_distance(origin, destination):
    try:
        # Use the distance_matrix function to calculate the distance
        matrix = gmaps.distance_matrix(origin, destination, units="metric", mode="driving")
        
        # Extract the distance value (in meters) from the response
        distance_in_meters = matrix["rows"][0]["elements"][0]["distance"]["value"]
        
        # Convert meters to kilometers
        distance_in_kilometers = distance_in_meters / 1000
        
        return distance_in_kilometers
    except Exception as e:
        return {"error": str(e)}

# Example coordinates (latitude and longitude)
latitude1 = 40.7128
longitude1 = -74.0060
latitude2 = 34.0522
longitude2 = -118.2437

origin_coords = (latitude1, longitude1)
destination_coords = (latitude2, longitude2)

distance = calculate_distance(origin_coords, destination_coords)
print(f"Distance: {distance} kilometers")
