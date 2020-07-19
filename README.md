kakao-arena-melon

본 repository는 kakao arena melon playlist continuation대회에 참가한 모델이다.
이 모델은 playlist의 tag, songs, title, genre 등을 임베딩하여 예측하고자 하는 playlist와 유사한 playlist를 찾아서
tag와 song을 예측한다.

임베딩 파일과 모델 파이프라인은 대회가 종료된 후에 업로드할 예정이다.


## p2v.ipynb
플레이리스트 요소(title, tag, song 등)의 벡터합으로 플레이리스트 벡터를 구한다.

## t2v.ipynb
제목을 형태소 분석한 후 각 토큰을 임베딩한다. 
이 후 각 토큰별 벡터를 합하여 제목을 하나의 벡터로 표현한다.

## get_result.ipyng
tag/song vector와 title vector를 활용하여 유사한 플레이리스트에서 다수 출현한 곡과 태그를 선별한다.

