from django.db import models
from django.urls import reverse # 모델형안에서는 리버스를 쓰지만 클래 클래스형 뷰 안에서는 필드값으로 쓸때 리버스 레이지를 써야함
# Create your models here.
# 모델 : 데이터베이스를 SQL 없이 다루려고 모델을 사용
# 우리가 데이터를 객체화해서 다루겠다.
# 모델= 테이블
# 모델의 필드 = 테이블의 컬럼
# 인스턴스 = 테이블의 레코드
# 필드의 값(인스턴스의 필드값) = 레코드의 컬럼 데이터값
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    # 필드의 종류가 결정하는것
    # 1. 데이베이스의 컬럼 종류
    # 2. 제약 사항 (몇글자까지)
    # 3. Form의 종류
    # 4. Form 에서 제약 사항

    def __str__(self):
        return "이름 : "+self.site_name+", 주소 : "+self.url
# 모델을 만들었다 => 데이터베이스에 어떤 데이터들을 어떤 형태로 넣을지 결정!
# makemigrations => 모델의 변경사항을 추적해서 기록
# 마이그레이션(migrate) => 데이터베이스 모델의 내용을 반영 (테이블 생성)
# 모델을 수정후 다시 마이그레이션 해야함
    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
# 업데이트 뷰를 쓸때 업데이트페이지 오류 뜰때 씀 pk 값이 필요함으로 이렇게 넣어줘야함
# 매개 변수로 넣어주는것이므로 디테일 뒤 디테일임으로 str 넣어도 되고 안넣어도되고