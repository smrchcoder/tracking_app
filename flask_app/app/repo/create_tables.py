# Create tables if they don't exist
from .create_cursor import connect_db
def create_tables_if_not_exist():
    try:
        conn ,cursor= connect_db()
        

        # Check if the 'GPS' table exists
        cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s)", ('GPS',))
        gps_table_exists = cursor.fetchone()[0]

        if not gps_table_exists:
            # Create the 'GPS' table if it doesn't exist
            cursor.execute('''
                CREATE TABLE GPS (
                    id SERIAL NOT NULL,
                    device_id TEXT NOT NULL,
                    timestamp TIMESTAMP NOT NULL,
                    longitude REAL NOT NULL,
                    latitude REAL NOT NULL
                )
            ''')

        # Check if the 'InitialCoordinates' table exists
        cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s)", ('InitialCoordinates',))
        initial_coords_table_exists = cursor.fetchone()[0]

        if not initial_coords_table_exists:
            # Create the 'InitialCoordinates' table if it doesn't exist
            cursor.execute('''
                CREATE TABLE InitialCoordinates (
                    device_id TEXT PRIMARY KEY,
                    longitude REAL NOT NULL,
                    latitude REAL NOT NULL,
                    destination_longitude REAL,
                    destination_latitude REAL
                )
            ''')

        conn.commit()
        conn.close()
        return {"message": "Tables created or already exist."}
    except Exception as e:
        return {"error": str(e)}