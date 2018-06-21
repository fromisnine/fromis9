import string
import random
import datetime

import subprocess
import os
from shutil import move



class Post:
  def __init__(self, date, post_type): #example : post(datetime,tag, video/photo..)
    self.date = str(date)[:19]+" +0900 KST"
    self.tags = [post_type]
    self.data = {
      'layout':'post',
      'current':'post',
      'cover':'',
      'navigation':'true',
      'title':'',
      'date':self.date,
      'tags':self.tags,
      'class':'post-template',
      'subclass' : f'post tag-{post_type}',
      'author': 'auto-posting'
    }
    self.body = ''
  
  def set_option(self, title, tags): # set_option("제목",['태그1','태그2'...])
    self.data['title'] = title
    self.data['tags'] = ' '.join(tags+self.data['tags'])
  
  def set_body(self,body,name,url):
    #msg = '> 본 게시물은 자동으로 작성된 게시물이며 추후 수정될 수 있습니다.\n'
    self.body = body
    self.body += f'\n\nPost by {name}\n\n'
    self.body += f'> [{name}]({url})'

  def random_gen(self,size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

  def set_cover(self,url):
    self.data['cover']=url

  def make_post(self,folder,name): # 폴더는 절대경로
    result = "---\n"
    for key, item in self.data.items():
      result += f'{key}: {item}\n'
    result += "---\n\n"
    result += self.body
    rand = self.random_gen()
    with open(f'{folder}/{self.date[:10]}-{name}-{rand}.md',"w") as f:
      f.write(result)
    print(f'{folder} 경로에 {name}님의 포스팅이 정상적으로 생성되었습니다.')

def commit_and_push(source,destination):
  src = source
  dst = destination
  files = os.listdir(src)

  print('[+]파일을 이동합니다.')
  for f in files:
    move(src+f,dst)
    print(f'[+]{f} 파일이 이동되었습니다.')

  print('\n[+]파일 이동 완료')
  
  os.chdir(destination)
  subprocess.call(["git", "pull"])
  subprocess.call(["git", "add", "."])
  subprocess.call(["git", "commit", "-m", "auto-post"])
  subprocess.call(["git", "push", "-u", "origin", "master"])
  print('[+] 저장소로 push가 완료되었습니다')
    
'''
#사용예시
p = Post( date ,'photo')
p.set_option('title 들어가는 곳',['태그1', '태그2'])
p.set_body('```\n이곳은 본문\nㅎㅎㅎ이것도\n#hello\n```\n','임재연','https://fromis9.kr')
p.make_post('./')
'''