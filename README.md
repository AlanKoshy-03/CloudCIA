### Song-Player
# Overview
This is a simple Spotify-like music streaming app built using Django. It allows users to select songs based on mood, control playback, adjust the volume, and navigate through the song playlist. The songs are served from the app's static directory, ensuring seamless local playback.

# Features
Mood-based Song Selection: Users can choose from a list of predefined moods, and the app will filter and display songs based on the selected mood.

Playback Controls: Includes essential controls for playing, pausing, and skipping to the next or previous songs.

Volume and Mute Controls: Users can adjust the playback volume or mute the sound entirely.

Seek Bar: Provides the ability to jump to a specific part of the song.

Dynamic Background: The background of the app changes based on the currently playing song, giving a more immersive experience.

Static Audio Hosting: Songs are hosted within the app’s static files, ensuring fast and reliable playback without external dependencies.

# Installation
1. Clone the repository:

bash
Copy code
git clone https://github.com/AlanKoshy-03/CloudCIA.git
cd Song_Player  
2. Install dependencies:

bash
Copy code
pip install -r requirements.txt  
3. Set up Django:

bash
Copy code
python manage.py migrate  
python manage.py collectstatic  
4. Run the server:

bash
Copy code
python manage.py runserver  
Visit http://127.0.0.1:8000/ to access the app.

Configuration
Make sure the songs are placed in the static/audio/ folder in your Django app. Update the song metadata (name, file paths, mood) in the database or directly within the Django views.

# Usage
1. Select a mood:
Users can choose a mood from the dropdown, and the app will load and display songs accordingly.

2. Control playback:
You can use the play, pause, next, and previous buttons to control the songs. Additionally, there is a seek bar to skip through the track and volume control to adjust the audio.

3. Enjoy the dynamic interface:
The background changes based on the song being played, providing a dynamic user experience.

# File Structure
main_page.html: The main interface for the app, containing HTML and JavaScript code for song control and dynamic background changes.

views.py: Django views to handle the logic of loading songs based on mood and serving audio files.

urls.py: URL routing to map web requests to the correct views.

static/audio/: Directory where the audio files are stored.

static/: Contains static files like CSS, images, and JavaScript.

templates/: Stores the HTML templates for rendering the app’s UI.

requirements.txt: Lists all the dependencies required to run the app.

# Future Enhancements
User Authentication: Allow users to sign in and save playlists or preferences.
Database Integration: Store song metadata and user preferences in a database for easier management.
Improved UI Design: Add more modern styles and transitions for a better user experience.
Acknowledgements
Django for providing the framework to build the app.

HTML, CSS, and JavaScript for building the frontend and controlling the playback functionalities.

Open-source libraries and tools for simplifying the development process.

# Contact
For any questions or feedback, please contact:
alan.bobby03@gmail.com
