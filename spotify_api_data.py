import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import pandas as pd

class SpotifyAPI:
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope
    
    def spotify_connection(self):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id,
                                                       client_secret=self.client_secret,
                                                       redirect_uri=self.redirect_uri,
                                                       scope=self.scope))
        return sp
        
    def get_top_tracks(self, time_range):
        sp = self.spotify_connection()
        top_tracks = sp.current_user_top_tracks(limit=40, offset=0, time_range=time_range)
        return top_tracks
    
    def get_track_ids(self, top_tracks):
        track_ids = []
        for song in top_tracks['items']:
            track_ids.append(song['id'])
        return track_ids
    
    def get_track_info(self, track_id):
        sp = self.spotify_connection()
        data = sp.track(track_id)
        name = data['name']
        album = data['album']['name']
        artist = data['album']['artists'][0]['name']
        spotify_url = data['external_urls']['spotify']
        track_info = [name, album, artist, spotify_url]
        return track_info
    
    def list_tracks(self, track_ids_list):
        sp = self.spotify_connection()
        tracks = []
        for i in range(len(track_ids_list)):
            time.sleep(1)
            track = self.get_track_info(track_ids_list[i])
            tracks.append(track)
        return tracks

    def create_df_list(self, your_tracks_list):
        df = pd.DataFrame(your_tracks_list,columns = ['name','album','artist','spotify_url'])
        return df
    
    def load_csv(self, df):
        df.to_csv('spotify_wrapped.csv',header=True,index=False)