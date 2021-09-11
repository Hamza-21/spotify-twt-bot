import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#authorization
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id= '62918d4efeb1493b871cf429f92d1881', client_secret='eb5196981e9442f8bfdbbcfbb6598db1',))

pl_id = "spotify:playlist:4d5Pl5U5aVE9xS3bUozxMr" #playlist id, can also be declared in the method

data = spotify.playlist_tracks(pl_id,)
tracks = data['items']

#for extending paged results, i.e. going over 100 song limit
while data['next']:
    data = spotify.next(data)
    tracks.extend(data['items'])

sys.stdout = open("pl_info2.txt", "w") #printing output in a file

for i in range(len(tracks)):
    songs = tracks[i]
    primary_info = songs["track"]
    primary_url = primary_info["external_urls"]
    print(i+1, primary_info["name"])
    print(primary_url["spotify"])


sys.stdout.close()