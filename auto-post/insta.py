import requests
import re
import datetime
import json
from bs4 import BeautifulSoup as bs
import dateutil.parser
import fromis9

print('[REPLAY] 인스타 fromis9.kr 자동 포스팅 생성')
urls = input('인스타 글 주소 : ').replace('/?taken-by=officialfromis_9',"").split(',')#'https://www.instagram.com/p/BkPVVWBFpIE/'

for url in urls:
  # 사용자 아이디, 이름, 태그 생성
  if url[-1] =='/':
    url = url[:-1]
  api_url = f'https://api.instagram.com/oembed/?url={url}/&hidecaption=0'
  req = requests.get(api_url)
  j_data = json.loads(req.text) # 인스타 api이용 글 정보 수집
  soup = bs(j_data['html'],'html.parser')

  user_id = j_data['author_name']
  user_name = j_data['author_name']
  name_tag = [user_name.replace(' ','-')]

  # 작성시간 저장 -> t_date
  t_date = soup.find('time')['datetime']
  t_date = dateutil.parser.parse(t_date)

  #사진 추출
  photo = j_data['thumbnail_url']
  if photo != None: # 이미지 있으면

    #본문 텍스트 추출
    text = j_data['title']
    link = j_data['author_url']

    text = '```\n'+text+'\n```\n\n'

    #blockquote 부분추가
    text += j_data['html']

    # imgs = [tag['src'] for tag in photo.find_all('img')]
    # for i,img in enumerate(imgs):
    #   text += f'![{i}]({img})\n'
      
    
    n_post = fromis9.Post(t_date,'photo')
    n_post.set_cover(photo)
    n_post.set_option(f'{user_name} instagram post',name_tag)
    n_post.set_body(text,user_name,f'https://www.instagram.com/{user_id}')
    n_post.make_post('./posts',user_name)
  else:
    print('사진이 없습니다. 다음 포스팅을 진행합니다..')

flag = input('바로 커밋 하시겠습니까? [default:y] : ')

if (flag == "" or flag == "y"):
  fromis9.commit_and_push('./posts/','../../fromis9/_posts/photo/insta/auto')






