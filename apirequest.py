import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET


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


def searchSongs(login, track="", artist="", album=""):
    results = []

    query = ("", "track: " + track + " ")[track != ""] + \
            ("", "artist: " + artist + " ")[artist != ""] + \
            ("", "album: " + album + " ")[album != ""]

    search = login.search(q=query, type="track")

    for track in search["tracks"]["items"]:
        results.append({
            "track": track['name'],
            "album": track["album"]["name"],
            "artists": [name["name"] for name in track["artists"]],
            "cover": track['album']['images'][0]['url']
        })

    return results
