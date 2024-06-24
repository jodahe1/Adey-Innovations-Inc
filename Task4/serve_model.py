from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Establish a connection to the PostgreSQL database
def create_connection():
    conn = psycopg2.connect(
        host="local",
        port="5542",
        database="week8",
        user="postgres",
        password="postgres"
    )
    return conn

# Fetch data from the database
def fetch_data():
    conn = create_connection()
    cursor = conn.cursor()

    # Execute a SQL query
    cursor.execute("SELECT * FROM Frauddata")

    # Fetch all the rows as a list of tuples
    rows = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return rows

# Define an API endpoint to fetch the data
@app.route('/data', methods=['GET'])
def get_data():
    data = fetch_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)