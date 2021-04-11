import os.path
import json
import typing as tp
import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials

FILE_PATH: str = os.path.join('.', 'MyData')
SPOTIFY_CREDENTIALS_PATH: str = os.path.join('.', 'spotify_creds.json')

def get_spotify_data(file_type: str) -> tp.List[tp.Dict]:
    files = [f.path for f in os.scandir(FILE_PATH) if file_type in f.name]
    json_objs = []
    for file_name in files:
        with open(file_name, 'r') as f:
            json_objs.extend(json.load(f))
    return json_objs


def get_spotify_client():
    with open(SPOTIFY_CREDENTIALS_PATH, 'r') as f:
        creds_json = json.load(f)
        creds = SpotifyClientCredentials(client_id=creds_json['client_id'], client_secret=creds_json['client_secret'])
        token = creds.get_access_token()
        return sp.Spotify(auth=token)
