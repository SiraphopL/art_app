from flask import Flask, render_template
import mysql.connector
from config import db_config

app = Flask(__name__)

def get_artworks():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM artworks")
    artworks = cursor.fetchall()
    cursor.close()
    conn.close()
    return artworks

@app.route("/")
def index():
    artworks = get_artworks()
    return render_template("index.html", artworks=artworks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
