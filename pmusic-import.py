# coding: utf8
from gmusicapi import Mobileclient
import json
import sys

api = Mobileclient()
api.login("google-username", "google-password")

def find_songs(artist, title, album):
    pos_results = api.search_all_access(title)["song_hits"]
    def_results = filter(lambda res :
            ((res["track"]["albumArtist"] == artist) and (res["track"]["album"] == album)),
            pos_results)
    return def_results


def known_songids():
    songs = api.get_all_songs()
    return map(lambda song: 
            song["nid"] if ("nid" in song) else song["id"],
            songs)

rdio_tracks = json.loads(open("tracks.json").read())

known_songs = known_songids()

for track in rdio_tracks:
    songs = find_songs(track["artist"], track["title"], track["album"])
    if ( len(songs) > 0) :
        song = songs[0]
        if (not (song["track"]["nid"] in known_songs)):
            api.add_aa_track(song["track"]["nid"])
            print u"+ {} by {} from {}".format(track["title"], track["artist"], track["album"])
    else:
        print u"Could not find {} by {} from {} in Play music".format(track["title"], track["artist"], track["album"])

