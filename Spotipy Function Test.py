## Testing components

import spotipy
from spotipy.oauth2 import SpotifyOAuth

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import pandas as pd
import requests

cid = 'cf0cdde5141f4581a6ebeffa7ea1ef36'     #Client ID
secret = '557f8171d6fb43568dfef2a8407a3e17'     #secret ID

client_credentials_manager = SpotifyClientCredentials(client_id = cid, client_secret=secret)
#sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)



scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])