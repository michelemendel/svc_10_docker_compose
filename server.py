import os
from flask import Flask
import mysql.connector
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.route('/')
def index():
    # Test connection to the database
    config = {
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
        'user': os.getenv('DB_ROOT_USER'),
        'password': os.getenv('DB_ROOT_PASSWORD'),
        'database': os.getenv('DB_DATABASE')
    }

    print("Config:")
    print(config)

    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            return "Connection to the database successful"
        else:
            return "Connection to the database failed"
    except mysql.connector.Error as e:
        return f"Error connecting to the database: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)