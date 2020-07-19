from itertools import chain
from collections import deque, Counter

def return_att(song_series, song_meta_DF, att = None, song_gnr_DF = None):
#     att
    song_meta_DF = song_meta_DF
    song_gnr_DF = song_gnr_DF
    def find_meta(x): return song_meta_DF[song_meta_DF['id'] == int(x)]
    def find_song(x): return list(find_meta(x)['song_name'])[0]
    def find_album(x): return list(find_meta(x)['album_id'])[0]
    def find_gnr(x): return list(find_meta(x)['song_gn_gnr_basket'])[0]
    def find_gnr_name(x): return list(song_gnr_DF[song_gnr_DF['gnr_code'] == x]['gnr_name'])[0]
    def find_gnr2(x): return list(find_meta(x)['song_gn_dtl_gnr_basket'])[0]
    def find_year(x): return str(list(find_meta(x)['issue_date'])[0])[:4]
    def find_artist(x): return list(find_meta(x)['artist_id_basket'])[0]
    
    if att == 'song':
        tmp = map(find_song, song_series)
        return list(tmp)
    elif att == 'album':
        tmp = map(find_album, song_series)
        return list(tmp)
    elif att == 'gnr':
        tmp = list(map(find_gnr, song_series))
        tmp = list(set(chain(*tmp)))
        tmp2 = list(map(find_gnr_name, tmp))
        return list(set(tmp2))
    elif att == 'gnr2':
        tmp = list(map(find_gnr2, song_series)) 
        tmp = list(chain(*tmp))
        tmp2 = Counter(tmp)
        return len(tmp2.keys()), tmp2.most_common(n=1)[0][0], tmp2.most_common(n=1)[0][1]
    elif att == 'year':
        tmp = map(find_year, song_series)
        tmp2 = Counter(tmp)
        return len(tmp2.keys()), int(tmp2.most_common(n=1)[0][0]), tmp2.most_common(n=1)[0][1]
    elif att == 'artist':
        tmp = list(map(find_artist, song_series))
        tmp = list(chain(*tmp))
        tmp2 = Counter(tmp)
        return len(tmp2.keys()), tmp2.most_common(n=1)[0][0], tmp2.most_common(n=1)[0][1]
    else:
        return len(song_series)

def mkDF4Cls(train_DF, song_meta_DF, song_gnr_DF):
    return_DF = pd.DataFrame()
    return_DF = train_DF[['id','plylst_title']]
    return_DF['num_song'] = train_DF['songs'].map(lambda x : return_att(deque(x),song_meta_DF))
    return_DF['song_name'] = train_DF['songs'].map(lambda x : return_att(deque(x),song_meta_DF, 'song'))
    return_DF['album_id'] = train_DF['songs'].map(lambda x : return_att(deque(x),song_meta_DF, 'album'))
    return_DF['gnr'] = train_DF['songs'].map(lambda x : return_att(deque(x),song_meta_DF, 'gnr', song_gnr_DF))
    return_DF[['num_gnr_dtl','first_gnr_dtl','num_first_gnr_dtl']] = pd.DataFrame(train_DF['songs'].map(lambda x : return_att(deque(x),song_meta_DF, 'gnr2')).tolist())
    return_DF[['num_year','first_year','num_first_year']] = pd.DataFrame(train_DF['songs'].map(lambda x : return_att(deque(x),song_meta_DF, 'year')).tolist())
    return_DF[['num_artist','first_artist','num_first_artist']] = pd.DataFrame(train_DF['songs'].map(lambda x : return_att(deque(x),song_meta_DF, 'artist')).tolist())
    return return_DF
