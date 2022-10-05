## File for attempting to mine my data from the Spotify API

#Client ID: cf0cdde5141f4581a6ebeffa7ea1ef36
#Client Secret: 557f8171d6fb43568dfef2a8407a3e17

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import pandas as pd
import requests

cid = 'cf0cdde5141f4581a6ebeffa7ea1ef36'     #Client ID
secret = '557f8171d6fb43568dfef2a8407a3e17'     #secret ID

client_credentials_manager = SpotifyClientCredentials(client_id = cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)



## TEST CODE TO SORT THROUGH PUBLIC SPOTIFY DATA ##
artist_name = []
track_name = []
popularity = []
track_id = []

for i in range(0,10,10):
    track_results = sp.search(q='year:2022 genre:indie genre:alt genre:rock', type='track', limit=10,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])


track_dataframe = pd.DataFrame({'artist_name' : artist_name, 'track_name' : track_name, 'track_id' : track_id, 'popularity' : popularity})
print(track_dataframe)
track_dataframe.head()

#print(track_dataframe)
######################################################

### Get information
 # URLS
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'

# Set scope
scope = 'user-library-read' # user-read-recently-played user-read-currently-playing'

#auth_code = requests.get(AUTH_URL, {
#    'client_id': cid,
#     'response_type': 'code',
#      'redirect_uri': 'https://open.spotify.com/collection/playlists',
#    'scope': scope  
#    })


## GET ACCESS TOKEN ##
data = {    
    'grant_type': 'client_credentials',
    'client_id': cid,
    'client_secret': secret,
    'scope': scope,
    'redirect_uri': 'https://open.spotify.com/collection/playlists',
}
auth_response = requests.post(TOKEN_URL, data = data)
#print(auth_response.text)
## END GET ACCESS TOKEN ##

## With access token ##
#from spotipy.oauth2 import SpotifyOAuth
#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
#results = sp.current_user_saved_tracks()
#for idx, item in enumerate(results['items']):
#    track = item['track']
#    print(idx, track['artists'][0]['name'], " – ", track['name'])








#access_token = auth_response.json().get('access_token')
#print(access_token)

#birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
#
#results = sp.artist_albums(birdy_uri, album_type='album')
#albums = results['items']
#while results['next']:
#    results = sp.next(results)
#    albums.extend(results['items'])
#
#for album in albums:
#    print(album['name'])