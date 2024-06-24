from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/api/data')
def get_data():
    conn = psycopg2.connect(
        host="localhost",
        database="week8",
        user="postgres",
        password="postgres"
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM CleanedCsv")  # Replace "your_table" with the actual table name

    data = cur.fetchall()

    cur.close()
    conn.close()

    return str(data)  # Returning the fetched data as a string for simplicity

if __name__ == '__main__':
    app.run()