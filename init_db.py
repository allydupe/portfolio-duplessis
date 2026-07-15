import sqlite3

conn = sqlite3.connect("jukebox.db")
c = conn.cursor()

c.execute("""
CREATE TABLE songs (
    id INTERGER PRIMARY KEY,
    title TEXT NOT NULL,
    artist TEXT NOT NULL,
    mood TEXT NOT NULL
)
""")

songs = [
    ("Centuries", "Fall Out Boy", "confident"),
    ("Here Comes the Sun", "The Beatles", "happy"),
    ("Someone Like You", "Adele", "sad"),
    ("Weightless", "Marconi Union", "relaxed")
]

c.executemany("INSERT INTO songs (title, artist, mood) VALUES (?, ?, ?)", songs)

conn.commit()
conn.close()
