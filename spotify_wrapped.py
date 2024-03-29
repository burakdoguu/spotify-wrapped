from spotify_api_data import SpotifyAPI

spotify_api = SpotifyAPI(client_id="your_id",
                         client_secret="Your_Secret_Key",
                         redirect_uri="http://mywrapped.com",
                         scope="user-top-read")

top_tracks_long = spotify_api.get_top_tracks(time_range="long_term")
track_ids = spotify_api.get_track_ids(top_tracks_long)
wrapped_list = spotify_api.list_tracks(track_ids)
df_track_list = spotify_api.create_df_list(wrapped_list)
load_csv_file = spotify_api.load_csv(df_track_list)
