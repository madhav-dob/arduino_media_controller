import spotipy
import spotipy.util as util
from requests import post, get, put
from dotenv import load_dotenv
import os
import json


load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
username = 'k2m6n7by28pglepu6b5kj8bhs'

# Scopes for Spotify API access
scope = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'

# Get user authorization
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

# if token:
#     sp = spotipy.Spotify(auth=token)
#     current_track = sp.current_playback()

#     while True:
#         # Display current song name
#         if current_track is not None and current_track['is_playing']:
#             print("Now playing:", current_track['item']['name'])
#         else:
#             print("No song is currently playing.")

#         # Get user input
#         action = input("Enter action (play, pause, next, previous, exit): ").lower()

#         # Perform action
#         if action == 'play':
#             sp.start_playback()
#         elif action == 'pause':
#             sp.pause_playback()
#         elif action == 'next':
#             sp.next_track()
#         elif action == 'previous':
#             sp.previous_track()
#         elif action == 'exit':
#             break
#         else:
#             print("Invalid action. Please try again.")

#         # Get current track
#         current_track = sp.current_playback()

# else:
#     print("Unable to get token for", username)

def get_auth_header(token):
    return{"Authorization": "Bearer " + token}

def currently_playing_song(token):
    url = "https://api.spotify.com/v1/me/player/currently-playing"
    headers  = get_auth_header(token)
    result = get(url, headers= headers)
    json_result = json.loads(result.content)
    return json_result['item']['name']

# def top_items(token):
#     url = "https://api.spotify.com/v1/me/top/artists"
#     headers  = get_auth_header(token)
#     result = get(url, headers= headers)
#     # json_result = json.loads(result.content)
#     # return json_result
#     return result


# def next_song(token):
#     url = "https://api.spotify.com/v1/me/player/next"
#     headers  = get_auth_header(token)
#     data = {"device_id":"213e5c8783119c94e040f4fc560c80bb74ca8e1e"}
#     result = post(url, headers= headers, data= data)
#     # json_result = json.loads(result.content)
#     # return json_result
#     return result

# def prev_song(token):
#     url = "https://api.spotify.com/v1/me/player/previous"
#     headers  = get_auth_header(token)
#     result = post(url, headers= headers)
#     # json_result = json.loads(result.content)
#     # return json_result
#     return result

# def pause_song(token):
#     url = "https://api.spotify.com/v1/me/player/devices"
#     headers  = get_auth_header(token)
#     result = get(url, headers= headers)
#     json_result = json.loads(result.content)
#     return json_result
#     # return result



result = currently_playing_song(token)

print(result)