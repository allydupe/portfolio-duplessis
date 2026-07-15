# Mood Jukebox

**Video Demo:**
https://somup.com/cT1OfCLkin

## Description

**Mood Jukebox** is a web based music app that allows users to select a mood and recieve a song recommendation.Built using **Flask** for the backend, **Javascript** for interactivity, and **SQLite** as a lightweight database, this project was created for CS50's final project.
The inspiration came from the way music can mirror and shift our emotions. I wanted to build something personal, intuitive, and fast. I also wanted to make it simple. I can see people from the IDD community using it to communicate emotions through music, especially those on the autism spectrum.

---

### Quick Overview of How It Works

When users visit the site, they're greeted with a simple interface where the can choose from moods like **happy**, **sad**, **confident**, or **relaxed**. Once a mood is selected:

- A 'POST' request is sent to the backend.
- FLASK queries the SQLite database.
- Matching songs are returned as a 'JSON' object.
- Javascript updates the page without needing a refresh.

---

### In More Detail

Mood Jukebox is designed to be as simple and smooth as possible for the user. Here’s how everything comes together behind the scenes:

- **User selects a mood**
   When someone visits the website, they’ll see a few buttons labeled with different moods—like *happy*, *sad*, *confident*, or *relaxed*. All they have to do is click the one that matches how they’re feeling.

- **The browser sends a message to the server**
   As soon as the user clicks a mood, a small bit of code written in JavaScript sends a **POST request** to the server. This request includes the selected mood.

- **Flask (the backend) receives the request**
   The server, built using **Flask**, catches the request and reads the mood the user chose. Then it looks inside the database to find a song that matches that mood.

- **The database is searched for a match**
   The database is a simple **SQLite** file that stores a list of moods and song recommendations. Flask runs a query that says something like “Find a song where the mood is happy.”

- **The result is sent back to the browser**
   If a match is found, Flask sends the song information (title, artist, and a short description) back to the browser as a **JSON object**.

- **The song appears instantly on the page**
   JavaScript takes that information and updates the webpage to show the song—without reloading the page. Everything happens instantly and seamlessly.

This process helps create a fast, interactive experience. There's no need to click through multiple pages or wait for things to reload. The user simply chooses how they feel, and a matching song appears right away.

### Project Structure
- 'appy.py' - Main Flask application that handles routing and serves the homepage and API endpoint.
- 'int_db.py' - Script that sets up and populates the 'songs' table in 'jukebox.bd' with intital tracks.
- 'jukebox.db' - SQLite database that stores song data.
- 'templates/index.html' - The HTML structure with embedded Javascript for mood selection and DOM updates.
- 'static/styles.css' - Clean and minimal CSS defining fonts, spacing , and layout, louded through Flask's static folder.

---

### Design Choices

- **No external APIs** — Everything is local for a self-contained, reliable experience.
- **Vanilla JavaScript** — No frameworks, just plain logic to better understand data flow.
- **Minimal UI** — A clean, modern interface with subtle design that centers on function.

---

### Future Enhancements

- Dynamic background color based on mood.
- Embedded audio previews for songs.
- User-submitted moods and songs.
- Integration with a larger music API for expanded recommendations.
- building a larger database using my own personal playlist.

---

### Final Thoughts

Mood Jukebox is a small but complete app that represents what I’ve learned during my time in CS50. It merges creativity, logic, and emotional intelligence into a single tool that’s both functional and expressive. I created everything myself—from the structure of the database and the backend routing to the frontend JavaScript and visual layout.

What makes me most proud is that this project feels like an honest reflection of my growth. It doesn’t try to do too much, but it does exactly what I wanted. It responds to a human feeling with something beautiful. Mood Jukebox taught me how to think across the full stack—how to move data, how to handle user input, and how to build something that responds in real time.

I hope anyone who uses it feels a little spark of joy, clarity, or comfort and maybe finds a new favorite song along the way.
