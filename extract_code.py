import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime
import pprint


def lambda_handler(event, context):
    
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    playlist_link = "https://open.spotify.com/playlist/5ABHKGoOzxkaa28ttQV9sE"
    playlist_URL = playlist_link.split("/")[-1]
    data = sp.playlist_tracks(playlist_URL)
    
    client = boto3.client('s3')
    filename = "spotify_raw_data" + str(datetime.now()) + ".json"

    client.put_object(
        Bucket="etlmuhammed",
        Key='raw_data/to_process/' + filename,
        Body=json.dumps(data)
        )