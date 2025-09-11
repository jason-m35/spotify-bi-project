import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
))

# Example: Taylor Swift top tracks in the US
artist_uri = "https://open.spotify.com/artist/5y8tKLUfMvliMe8IKamR32?si=BcqA0NRiSQyI-jBCpqKB7A"  # Taylor Swift
top_tracks = sp.artist_top_tracks(artist_uri, country="US")

for i, track in enumerate(top_tracks["tracks"][:5], start=1):
    print(f"{i}. {track['name']} (popularity {track['popularity']})")
