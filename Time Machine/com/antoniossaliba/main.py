from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import base64
from pprint import pprint

THE_URL         = os.environ.get("THE_URL")
CLIENT_ID       = os.environ.get("CLIENT_ID")
CLIENT_SECRET   = os.environ.get("CLIENT_SECRET")
REDIRECT_URI    = os.environ.get("REDIRECT_URI")
AUTH_CODE       = os.environ.get("AUTH_CODE")
TOKEN           = os.environ.get("TOKEN")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
))

def get_track_id(track_name):
    """Searches Spotify for a track name and returns its ID."""
    result = sp.search(q=track_name, type='track', limit=1)
    items = result['tracks']['items']
    if items:
        track = items[0]
        return {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'id': track['id'],
            'uri': track['uri']
        }
    return None

# Getting the Token in order to use the API
# parameters = {
#     "grant_type": "authorization_code",
#     "code": AUTH_CODE,
#     "redirect_uri": REDIRECT_URI
# }
#
# headers = {
#     "Authorization": "Basic " + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode(),
#     "Content-Type": "application/x-www-form-urlencoded"
# }
#
# response = requests.post(url="https://accounts.spotify.com/api/token",
#                          data=parameters,
#                          headers=headers)
#
# response.raise_for_status()
# print(response.json())

#Creating the playlist
user_id = requests.get(url="https://api.spotify.com/v1/me",
                       headers={"Authorization": f"Bearer {TOKEN}"})
user_id.raise_for_status()
pprint(user_id.json())

prompt = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

data = {
    "name": f"Top 100 Songs in {prompt}",
    "description": f"Listen to the top songs back on {prompt}",
    "public": True
}

head = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

res = requests.post(url=f"https://api.spotify.com/v1/users/{user_id.json()['id']}/playlists",
                    json=data,
                    headers=head)

res.raise_for_status()
pprint(res.json())
playlist_id = res.json()["id"]

# Scraping the website for the top 100 songs for the specified date
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
}
response1 = requests.get(url=f"https://www.billboard.com/charts/hot-100/{prompt}",
                        headers=header)
response1.raise_for_status()
soup = BeautifulSoup(response1.text, "html.parser")
all_title_tags = soup.select("li #title-of-a-story")
all_titles = []
for tag in all_title_tags:
    all_titles.append(tag.text.strip())

#Iterating through all the songs having the titles in all_titles and getting their URIs into the list_of_song_uris list
list_of_song_uris = []
for title in all_titles:
    info = get_track_id(title)
    try:
        id = info["id"]
        response2 = requests.get(url=f"https://api.spotify.com/v1/tracks/{id}",
                                 headers={"Authorization": f"Bearer {TOKEN}"})
        list_of_song_uris.append(info["uri"])
    except KeyError:
        pass

# Getting the tracks with the corresponding URLs in list_of_song_uris into the playlist
response3 = requests.post(url=f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks",
                          headers={"Authorization": f"Bearer {TOKEN}", 'Content-Type': 'application/json'},
                          json={"uris": list_of_song_uris, "position": 0})
response3.raise_for_status()