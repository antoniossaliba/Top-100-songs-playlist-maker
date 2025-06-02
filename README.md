# 🎵 Playlist Maker - Top 100 Songs by Date

This Python project allows users to generate a playlist of the top 100 songs on a specific date (in `YYYY-MM-DD` format). It scrapes the Billboard Hot 100 chart for that date and creates a corresponding playlist on your Spotify account.

## 🚀 Features

- Fetches Billboard Hot 100 songs for a specified date
- Authenticates with your Spotify account using OAuth
- Creates a private playlist and populates it with found songs
- Handles missing songs gracefully

## 🛠️ Requirements

- Python 3.7+
- Spotify Developer Account
- Spotify App Credentials (Client ID, Client Secret, Redirect URI)

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/playlist-maker.git
   cd playlist-maker
📅 Usage
Run the script and enter a date in the format YYYY-MM-DD:

bash
Copy
Edit
python main.py
The script will:

Fetch the Billboard Hot 100 songs for that date

Search for the songs on Spotify

Create a new private playlist titled "Top 100 from YYYY-MM-DD"

Add the found songs to your playlist

🧠 Example
css
Copy
Edit
Enter a date (YYYY-MM-DD): 2010-08-14
✅ Playlist 'Top 100 from 2010-08-14' created successfully on your Spotify account!
⚙️ Dependencies
requests

BeautifulSoup4

spotipy

python-dotenv

📌 Notes
Not all songs from the Billboard list may be available on Spotify.

Playlist creation requires permission to modify your Spotify library.

The script creates public playlists by default.

👨‍💻 Author
Your Name – @antoniossaliba

📝 License
This project is licensed under the MIT License. See the LICENSE file for details.
