import os.path
import json
import typing as tp

FILE_PATH: str = os.path.join('.', 'MyData')

def get_spotify_data(file_type: str) -> tp.List[tp.Dict]:
    files = [f.path for f in os.scandir(FILE_PATH) if file_type in f.name]
    json_objs = []
    for file_name in files:
        with open(file_name, 'r') as f:
            json_objs.extend(json.load(f))
    return json_objs
