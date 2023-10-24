import pytest
from spotify_api_data import SpotifyAPI
import os


@pytest.fixture
def spotify_api():
    return SpotifyAPI(client_id="Your_ID",
                      client_secret="Your_Secret_Key",
                      redirect_uri="http://mywrapped.com",
                      scope="user-top-read")

def test_spotify_connection(spotify_api):
    sp = spotify_api.spotify_connection()
    assert sp is not None


def test_get_top_tracks(spotify_api):
    top_tracks_long = spotify_api.get_top_tracks('long_term')
    track_ids = spotify_api.get_track_ids(top_tracks_long)
    assert len(track_ids) > 0

def test_list_tracks(spotify_api):
    top_tracks_long = spotify_api.get_top_tracks('long_term')
    track_ids = spotify_api.get_track_ids(top_tracks_long)
    wrapped_list = spotify_api.list_tracks(track_ids)
    assert len(wrapped_list) == 40

def test_load_csv(spotify_api):
    top_tracks = spotify_api.get_top_tracks('short_term')
    track_ids = spotify_api.get_track_ids(top_tracks)
    tracks = spotify_api.list_tracks(track_ids)
    df = spotify_api.create_df_list(tracks)
    spotify_api.load_csv(df)
    # Check if file exists

    assert os.path.exists('spotify_wrapped.csv')
