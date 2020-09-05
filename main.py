import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2
import pandas as pd
import os

market = [ "AD", "AR", "AT", "AU", "BE", "BG", "BO", "BR", "CA", "CH", "CL", "CO", "CR", "CY", 
      "CZ", "DE", "DK", "DO", "EC", "EE", "ES", "FI", "FR", "GB", "GR", "GT", "HK", "HN", "HU", 
      "ID", "IE", "IS", "IT", "JP", "LI", "LT", "LU", "LV", "MC", "MT", "MX", "MY", "NI", "NL", 
      "NO", "NZ", "PA", "PE", "PH", "PL", "PT", "PY", "SE", "SG", "SK", "SV", "TH", "TR", "TW", 
      "US", "UY", "VN" ]

def create_spotify():

      scope = "user-top-read user-library-read playlist-read-private playlist-read-collaborative"
      client_id = os.environ['CLIENT_ID']
      client_secret = os.environ['CLIENT_SECRET']
      user_name = os.environ['USER_NAME']
      redirect_uri = "http://example.com/callback/"
      token = util.prompt_for_user_token(username=user_name,scope=scope,client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri)
      s = spotipy.Spotify(auth=token)
      return(s)

s = create_spotify()

top_artists = s.current_user_top_artists(limit=20, offset=0, time_range='short_term')
for item in top_artists['items']:
    print(item['name'])

top_tracks = s.current_user_top_tracks(limit=20, offset=0, time_range='short_term')
for item in top_tracks['items']:
    print(s.audio_features(item['uri']))

s.current_user_saved_tracks()