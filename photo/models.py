from django.db import models

# Create your models here.

# 1. 모델 : 데이터베이스 저장될 데이터가 있다면 해당 데이터를 묘사한다.
# 2. 뷰(기능) : 계산, 처리 - 실제 기능, 화면
# 3. url 맵핑 : 라우팅 테이블에 기록한다. urls.py에 기록 - 주소를 지정
# 4. 화면에 보여줄 것이있다 : 템플릿작성(html)


# 장고의 기본 유저 모델
from django.contrib.auth.models import User
from django.urls import reverse


# 왜래키 (ForeingKey) - User 테이블에서 해당 유저를 찾을 수 있는 주키
# 주키 (PrimaryKey) - User 테이블에 1 admin x x x x
class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # makemigrations -> migrate
    class Meta:
        ordering = ['-updated']  #- 면 디샌딩 제일 마지막으로 설정 , 찍어서 중첩할수있음

    def __str__(self): #프린트를 해보거나 관리자 페이지에서 출력할때 씀
        return self.author.username + "" + self.created.strftime("%Y-%m-%d %H:%M:%S") #몇년 몇월 몇일 몇시 몇분 몇초에 생성되게끔 설정해주면됨

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[self.id])