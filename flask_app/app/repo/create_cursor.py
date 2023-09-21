import psycopg2
from app import app

def connect_db():
    conn = psycopg2.connect(app.config['DATABASE_URL'])
    cursor = conn.cursor()  # Create a cursor from the connection
    return conn, cursor  # Return both the connection and the cursor
