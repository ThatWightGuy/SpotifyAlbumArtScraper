from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def login():
    scope = "user-library-read"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope=scope,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri="http://localhost:8000",
        username='username')
    )

    return sp

results = login().search(q="artist: Radiohead", type="artist")
items = results['artists']['items']

if len(items) > 0:
    artist = items[0]
    print(artist)