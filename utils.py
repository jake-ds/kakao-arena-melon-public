import pandas as pd

def load_data():
    train = pd.read_json('data/train.json')
    val = pd.read_json('data/val.json')
    song_meta = pd.read_json('data/song_meta.json')
    
    return train, val, song_meta


### input song index list or str or int, return song name 
def get_song_name(songs):
    if type(songs) == list:
        return [song_meta[song_meta["id"]==int(song)]["song_name"].item() for song in songs]
    
    elif type(songs) == str or type(songs)== int:
        return song_meta[song_meta["id"]==int(songs)]["song_name"].item()