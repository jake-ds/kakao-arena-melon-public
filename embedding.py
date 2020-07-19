from tqdm import tqdm
import pandas as pd
from gensim.models import Word2Vec
from gensim.models.keyedvectors import WordEmbeddingsKeyedVectors
from datetime import datetime


def get_time():
    now = datetime.now()
    return now.isoformat()[:-7]


def get_token_data(train, val):

    total = []
    
    data = pd.concat([train, val], axis=0)
    
    for tags, id_, songs in zip(data["tags"], data["id"], data['songs']):
        songs = [str(x) for x in songs]
        total.append(songs+tags)
    
    total = [x for x in total if len(x)>1]
    
    return total

def get_s2v_model(total, min_count, size, window, sg):
    s2v_model = Word2Vec(total, min_count = min_count, size = size, window = window, sg = sg)

    file_name = "./manual_emb/s2v_mdl_" + get_time() + ".model"
    s2v_model.save(file_name)
    
    return  s2v_model


def get_p2v_model(train, val, w2v_model):
    p2v_model = WordEmbeddingsKeyedVectors(100)
    ID = []   
    vec = []
    data = pd.concat([train, val], axis=0)
    for id_, songs, tags in zip(data['id'], data['songs'], data['tags']):
        tmp_vec = 0
        for token in songs+tags:
            try: 
                tmp_vec += w2v_model.wv.get_vector(str(token))
            except KeyError:
                pass
        if type(tmp_vec)!=int:
            ID.append(str(id_))    
            vec.append(tmp_vec)
    p2v_model.add(ID, vec)
    
    file_name = "./manual_emb/p2v_mdl_" + get_time() + ".model"
    p2v_model.save(file_name)
    
    return p2v_model


################################################


def get_song_info(song_id):
    
    print('='*100)
    try:
        print(song_meta[song_meta['id']==int(song_id)][['song_name', 'artist_name_basket']])
    except:
        print(song_id)
    
    print('='*100)
    
    for item in s2v_model.most_similar(song_id):

        try:
            print(song_meta[song_meta['id']==int(item[0])][['song_name', 'artist_name_basket']])
        except:
            print(item[0])
            

################################################
