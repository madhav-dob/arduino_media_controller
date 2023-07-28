import spotipy
import spotipy.util as util
from requests import post, get, put
from dotenv import load_dotenv
import os
import json
import keyboard
import serial
import time

#spotify setup

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
username = 'k2m6n7by28pglepu6b5kj8bhs'

# Scopes for Spotify API access
scope = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'

# Get user authorization
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)


#spotify functions to get auth. headers and to get current song name
def get_auth_header(token):
    return{"Authorization": "Bearer " + token}

def currently_playing_song(token):
    url = "https://api.spotify.com/v1/me/player/currently-playing"
    headers  = get_auth_header(token)
    result = get(url, headers= headers)
    json_result = json.loads(result.content)
    return json_result['item']['name']


#serial setup
SerialObj = serial.Serial('/dev/ttyACM0',9600)
time.sleep(3) 


SerialObj.timeout = 3 # set the Read Timeout
while True:
    
    received_string = SerialObj.readline().decode().strip()

    # Perform actions based on the received string
    if received_string == "Play":
        print("Play action")
        
        
        keyboard.press_and_release('ctrl+w')
        # Add your code here for the play action

    elif received_string == "Next":
        print("Next action")
        
        keyboard.press_and_release('ctrl+f10')
        time.sleep(0.3)
        curr_song = currently_playing_song(token)
        SerialObj.write(curr_song.encode())
        print(curr_song)
        # Add your code here for the next action

    elif received_string == "Prev":
        print("Previous action")
        
        keyboard.press_and_release('ctrl+f8')
        time.sleep(0.3)
        curr_song = currently_playing_song(token)
        SerialObj.write(curr_song.encode())
        print(curr_song)
        # Add your code here for the previous action

    elif received_string == "up":
        print("Up action")
        keyboard.press_and_release('ctrl+8')
        # Add your code here for the up action
    elif received_string == "down":
        keyboard.press_and_release('ctrl+0')
        print("Down action")
    # Add additional conditions for more commands if needed

    else:
        print("Unknown command:", received_string)




