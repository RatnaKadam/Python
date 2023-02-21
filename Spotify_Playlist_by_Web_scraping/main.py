import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# ------ WebScraping and taking data of any date from Billboard ------------#

URL = "https://www.billboard.com/charts/hot-100/"

date_input = input("Which year do you want the music? Type the date in this format YYYY-MM-DD: ")
year = date_input.split("-")

response = requests.get(f"{URL}/{date_input}")
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
song_list = soup.select(selector="div li ul li h3")
# creating a song list
music_name = [music.getText().strip() for music in song_list]

# --------- Spotify Authorization----------------#

Client_ID = "Generate_Client_ID"
Client_secret = "Generate_Client_Secret"
playlist_id = "Generate_Playlist_Id"
SPOTIFY_URI_LIST = []
# authorization
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Client_ID,
                                               client_secret=Client_secret,
                                               redirect_uri="Own_valid_email_for_authentication",
                                               scope=" playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"
                                               ))
user_id = sp.current_user()["id"]

# ----------------- Creating Playlist and adding songs --------------------#

# creating Spotify uri list
for music in music_name:
    sp_uri = sp.search(f"track: {music}, year:{year}", type="track")
    # print(sp_uri)
    try:
        uri = sp_uri["tracks"]["items"][0]["uri"]
        SPOTIFY_URI_LIST.append(uri)
    except IndexError:
        print(f"{music} doesn't exist in Spotify. Skipped")

# creating actual playlist on profile
my_list = sp.user_playlist_create(user=user_id, name="Billboard 100 top songs", public=False)
print(my_list)

# adding songs to playlist
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=SPOTIFY_URI_LIST)







