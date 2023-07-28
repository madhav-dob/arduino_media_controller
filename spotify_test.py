import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")

SPOTIPY_CLIENT_ID=client_id
SPOTIPY_CLIENT_SECRET=client_secret
SPOTIPY_REDIRECT_URI=redirect_uri
SCOPE = 'user-read-currently-playing user-modify-playback-state user-read-playback-state'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE))

top_tracks_short = sp.current_user_top_tracks()
print(top_tracks_short)
                                              