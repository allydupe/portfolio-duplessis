from flask import Flask, render_template, request, jsonify; import sqlite3

app= Flask(__name__)

def get_db():
    conn = sqlite3.connect("jukebox.db")
    conn.row_factory = sqlite3.Row
    return conn
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/songs", methods=["POST"])
def songs():
    mood = request.json.get("mood")
    conn = get_db()
    songs = conn.execute("SELECT * FROM songs WHERE mood = ?", (mood,)).fetchall()
    conn.close()
    return jsonify([dict(song) for song in songs])

if __name__ == "__main__":
    app.run()
