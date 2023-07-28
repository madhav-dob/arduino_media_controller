from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json



load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


print(client_id, client_secret)

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode(encoding="utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"

    }
    data = {"grant_type":"client_credentials"}
    result = post(url, headers = headers,data= data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return{"Authorization": "Bearer " + token}


def search_for_artist(token, atrist_name):
    url = "https://api.spotify.com/v1/search"
    headers  = get_auth_header(token)
    query = f"?q={atrist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers= headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print ("no artust")
        return none
    return json_result[0]


def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    
    headers  = get_auth_header(token)
    result = get(url, headers= headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

def currently_playing_song(token):
    url = "https://api.spotify.com/v1/me/player/currently-playing"
    headers  = get_auth_header(token)
    result = get(url, headers= headers)
    json_result = json.loads(result.content)
    return json_result




token = 'BQCzMc9Gnf1T6-gzxYRdHZRwGBAj0SJ3IbSiuwky48o0FhVCzt2ZPU2PQ4X3bqYhjQTiibvYCDigKYocZ_gVNbd3QIL6YcdigW4VbK-SWph-vRAowPf0-Io4oP3JK0mSVMc6Q32rLMXQ5bHeXaIdj1CGPVYcmZbNncbpoTgnP3eJRtQ1BJH7W3zN_5H_QQzl7CaJd1JLgPIKPyp1Pd0pAxAqaRyR1irxNJff6dQ840DxDf8d6-T2zaoxpt1Nh5xOBs_mleg2YqXxQmnXII7y'
result = currently_playing_song(token)

print(result)