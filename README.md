자동 배포 확인용 사이트 -> [travis-ci](https://travis-ci.org/)

# https://fromis9.kr 에 글을 쓰자!

모르는 내용이 있다면 https://github.com/fromisnine/fromis9/issues 를 통해 

```New issue``` 를 눌러 글을 남겨주시면 답변 드리겠습니다!

### 1. 일단 Github.com에 가입한다.

[github](https://github.com) 에 접속하여 

> Username : ID  
Email : 이메일  
Password : 비밀번호  

를 입력후 ```Sign Up for Github``` 를 눌러 가입한다.

메일로 도착한 이메일 인증 메일을 확인하고 

클릭하라는것 처럼 생긴 버튼을 눌러 인증을 완료한다!

## 끝!

----

### 2. https://github.com/fromisnine/fromisnine.github.io 에 들어가서 _post 클릭!

> _posts 에는 페이지의 모든글이 저장되어있다.

----

### 3. 폴더를 선택한다

* notice : 프로미스나인 공지사항, MD 판매물품등 공지사항
* photo : 사진들
* video : 유튜브, vlive 등 저장 용도
등등.. 찾아찾아 보면 적당한 폴더가 있다!

-----


### 4. Create New File 클릭!


md파일을 직접 만든 경우 업로드를 해도 무관하다.

이미지 파일을 저장하고 싶은 경우

다다음 내용에 나올 Pull Request 과정에서 메모로 남겨주면

확인후 개인폴더를 추가해준다!!! (되도록 링크를 가져다 쓰자..)

파일명은 꼭!! **년도-월-일-제목.md** 으로 작성한다. (그래야 포스트로 인식하고 등록된다.)

예시 : 2018-06-05-프로미스나인-사랑해♥.md

###  5. 내용작성

약 ~ 간 어려운 부분나왔다 드디어 내용을 쓰는 부분이다.

```
꿀 Tip한개 드리자면

1. fromis9.kr 페이지에서 자신이 쓰고싶은 글과 비슷한 글을 찾는다!

2. 그 글을 _post에서 찾는다! 
   video, photo등 글 제목으로 유추하거나 주소창에 있는 fromis9.kr/ [이 부분]
   
   저 글의 파일이름은 년도-월-일-[이 부분].md 일 것이다!
   
3. 그 글을 클릭한 후 내용을 복사 붙여넣기 한다음 필요한 부분만 고친다!
```

마지막줄이 핵심인 팁이었다.. (역시 답은 CTRL+c, CTRL+V...)


자 이제 글을 구성하는 요소에 대해 알아보자!

아무 md파일을 열어서 내용을 보면 가장 처음 부분에 ```---```문자로 둘러쌓인 부분이 보인다.

포스트의 제목, 태그 등을 설정하는 부분이다.

아래는 https://fromis9.kr/official_photo 의 전체 내용이다.

파일 위치는 ```_posts/photo/official/2018-06-10-official_photo.md``` 에서 찾을 수 있다.

간단한 설명만 붙이도록 하겠다.

```
---                  # 여기서부터 헤더 시작
layout: post         # 신경쓰지 않아도 됨 수정X
current: post        # 신경쓰지 않아도 됨 수정X

cover: 'http://media.fromisnine.com/wp-content/uploads/2018/05/25200607/fromis_9_Official-Photo.jpg' 
        # 게시글 커버이미지(썸네일,미리보기)
        
navigation: true     # 신경쓰지 않아도 됨 수정X
title: Fromis_9 Official-Photo  #게시글의 제목! '[' 문자와 ']' 문자, '#' 문자는 에러를 일으키므로 주의하자
date: 2018-06-10 00:00:00       #게시글의 시간이다. 언제 작성하든 그날의 날짜, 시간을 설정할수 있다(시간은 생략가능)
tags: photo 지헌 서연 지원 지선   #태그 목록이다. 띄어쓰기로 구분한다.
class: post-template             # 신경쓰지 않아도 됨 수정X
subclass: 'post tag-photo'        # 신경쓰지 않아도 됨 수정X
author: imreplay                   
# 글쓴이를 정해주는 부분이다. 글 쓸때 
사용할 ID(영어로)*, 표시될 이름*, 소개문구, 커버사진, 로고사진, 페북주소, 트위터주소 등 (* 필수)
을 Pull Request 내용에 같이 넣어주거나 글 밑에 써주면 페이지에 글쓰기 권한과 소개 페이지를 만들어준다!
그 후에는 author에 자신의 고유 ID를 넣으면 된다!

---                 #여기가 헤더끝 다음내용부터 글 내용

프로미스나인 (fromis_9) – The 2nd Mini Album [To. Day] Official Photo  #여기는 그냥 일반 텍스트

![Main Image](http://media.fromisnine.com/wp-content/uploads/2018/05/25200607/fromis_9_Official-Photo.jpg)

#여기 위에 보이는건 사진을 넣는 방법이다. ![사진설명](http://주소) 또는 ![사진설명](assets/img/~~~~/~~~.jpg) 처럼 사용가능하다.
```

역시 이해하기 힘든 언어인거같다..

자 그래도 우리에게는 무적의 Ctrl + C, Ctrl + V 가 있다.

다른 글을 새창으로 띄운 후 내용을 보면!

윗 부분은 살짝씩만 바꾸면 되니 이번엔 다른 본문으로 가자!

```
### 프로미스나인 공식 인스타그램 업데이트

> 롬쌔 언니의 사랑이 그득 담긴 사진이에요~
팬분들도 사랑해주실꼬 같아서 올릴꼬에욥💕  
> #메거니 #크롬쌔 #콜라보레이션 #쥐예아아

![지원](https://fromis9.kr/img/jiwon.jpg)
```

이 문장은 이렇게 표시됩니다.

### 프로미스나인 공식 인스타그램 업데이트

> 롬쌔 언니의 사랑이 그득 담긴 사진이에요~
팬분들도 사랑해주실꼬 같아서 올릴꼬에욥💕  
> #메거니 #크롬쌔 #콜라보레이션 #쥐예아아

![지원](https://fromis9.kr/img/jiwon.jpg)

---

어느정도 감이 오셨나요..?

### 6. Propose New File 버튼을 눌러 제출한다.



### 7. Create PullRequest 버튼(초록색) 을 누른다!



### 8. 사실 여기까지 왔으면 어찌 되었든 성공하셨습니다!

간략한 설명, 또는 요청할 내용을 넣어 준 후(안쓰셔도 괜찮아요!)
모르겠으면 모르겠어요.. 하고 URL, 출처만 보내주셔도 됩니다!! 
Create PullRequest 눌러줍니다!
그럼 저에게 띠링! 알림이 오고 확인 후에 

잘 못된 부분이 있는지 확인 및 수정 후 바로 업로드 합니다!

올라가기 전에 제가 수정할 수 있습니다! 편하게 막 쓰셔도 괜찮아요!


---


모르는 내용이 있다면 https://github.com/fromisnine/fromis9/issues 를 통해 

New issue 를 눌러 글을 남겨주시면 답변 드리겠습니다!
