import json
import requests
import urllib.parse as up
import datetime

import fromis9

url = "https://www.googleapis.com/youtube/v3/search?"

videoId = input("paste video id : ")
m_res = 3

parms = {
        'part':'snippet',
        'maxResults':m_res,
        'q':videoId,
        'key':'API key'
        }

url = url+up.urlencode(parms)

req = requests.get(url)
res = req.text

datas = json.loads(res)


print('\n프로미스나인(fromis_9) 의 Youtube 게시글을 검색합니다.')
print(datetime.datetime.now())


print('===========================================\n')

for data in datas['items']:
    v_title = data['snippet']['title'] #i번째 글의 영상 제목
    v_desc = data['snippet']['description'] #i번째 글의 영상 설명

    print(f'제목 : {v_title}')
    print(f'설명 : {v_desc}')
    print(f'주소 : https://www.youtube.com/watch?v={videoId}')
    print('\n===========================================\n\n')


