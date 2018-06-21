import requests
import re
import datetime
from bs4 import BeautifulSoup as bs

import fromis9

print('[REPLAY] 트위터 fromis9.kr 자동 포스팅 생성')
urls = input('트윗 주소 : ').split(',')#'https://twitter.com/BMO_fromis/status/1008805567303901184'


# 트위터 업로더 목록
user_list = {
  'BMO_fromis':'Beautiful My Ocean', #션
  'fromis_RJS':'Over The Sunrise', #지선
  'pitapat320':'pit a pat', #젼
  '000514net':'미루나무', #챙
  'leesaerom0107':'love in love',#롬
  'songforu_0929':'Song For U', #쏭
  'liking61':'Liking', #롬
  'MLBunny_929':'My little Bunny',#쏭
  'delightday_JS':'DELIGHT DAY', #지선
  '19980320_j_w_':'Journey With you', #지원
  'OrangeRoad8':'ORANGE ROAD', #all
  'LastClover_0514':'Last Clover', #채영
  'kkhoney0417':'꿀꿀허니', #지헌
  'Temperature_98':'오늘의 온도', #지원,지선
  '970929_net' : '송하영닷넷', #하영
  'Studio_NaGyung': 'SIGNAL', # 하영, 나경
  '9clover_' : 'NINE CLOVER TO HEART',
  'jiwon_is_pretty': '박지원 예쁘다', #지원
  'realfromis_9':'fromis_9' #공식
}
for url in urls:
  # 사용자 아이디, 이름, 태그 생성
  user_id = url.split('/')[3]
  try:
    user_name = user_list[user_id]
  except:
    user_name = user_id
  name_tag = [user_name.replace(' ','-')]

  req = requests.get(url)
  html = req.text
  soup = bs(html,'html.parser')

  # 작성시간 저장 -> t_date
  t_date = int(soup.find('small','time').find('span')['data-time'])
  t_date = datetime.datetime.fromtimestamp(t_date)

  #사진 추출
  photo = soup.find('div', 'AdaptiveMedia-container')
  if photo != None: # 이미지 있으면

    #텍스트 추출
    text = soup.find('div', 'js-tweet-text-container').get_text()
    #사진이있으면 뒤에 pic.twitter.com/b8QSUehCnd 가 붙는듯 제거필요함
    link = re.findall('pic.twitter.com/.+',text)[0]
    text = '```'+text.replace(link,"").replace('\n','  \n')+'\n```\n\n'

    imgs = [tag['src'] for tag in photo.find_all('img')]
    for i,img in enumerate(imgs):
      text += f'![{i}]({img})\n'
      
    
    n_post = fromis9.Post(t_date,'photo')
    n_post.set_cover(img)
    n_post.set_option(f'{user_name} twitter post',name_tag)
    n_post.set_body(text,user_name,f'https://twitter.com/{user_id}')
    n_post.make_post('./posts',user_name)
  else:
    print('사진이 없습니다. 다음 포스팅을 진행합니다..')

flag = input('바로 커밋 하시겠습니까? [default:y] : ')

if (flag == "" or flag == "y"):
  fromis9.commit_and_push('./posts/','../_posts/photo/twitter/auto/')


'''
#윈도우 버전
    n_post = fromis9.Post(t_date,'photo')
    n_post.set_cover(img)
    n_post.set_option(f'{user_name} twitter post',name_tag)
    n_post.set_body(text,user_name,f'https://twitter.com/{user_id}')
    n_post.make_post('c:\\Users\\Nirone\\Desktop\\pz\\my_files\\py\\fromis9\\posts',user_name)
  else:
    print('사진이 없습니다. 다음 포스팅을 진행합니다..')

flag = input('바로 커밋 하시겠습니까? [default:y] : ')

if (flag == "" or flag == "y"):
  fromis9.commit_and_push('c:\\Users\\Nirone\\Desktop\\pz\\my_files\\py\\fromis9\\posts\\','C:\\Users\\Nirone\\Desktop\\pz\\fromis9\\_posts\\photo\\twitter\\auto')

'''



