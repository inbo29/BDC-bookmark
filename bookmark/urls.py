from django.urls import path
from .views import *

# BookmarkListView , BookmarkCreateVeiw ,BookmarkDetailVeiw 이렇게 길게 써도되나 다써도 되나 * <이걸로 바꿔도 됨

urlpatterns = [
    # http://127.0.0.1/bookmark/???
    # 이게 있었으나 ""은 다떄고온다는뜻 -> ??? 이것만 남음 그러므로 본래적으로 http://127.0.0.1/bookmark/ 이것만 남음
    path("", home, name='home'),
    path("list/", BookmarkListView.as_view(), name='list'),

    # 클래스 형 뷰 일시 .as_view() 써야함 클래스형을 함수형으로 바꿔줌 함수형일 경우 이름만 쓰면됨
    # 앞에 "" 유형이 이름이 name='' 임
    path("add/", BookmarkCreateVeiw.as_view(), name='add'),
    # name 은 나중에 add/ 주소에서 템플랫 불러오는 용도로 쓰이는 이름임
    path("detail/<int:pk>/", BookmarkDetailVeiw.as_view(), name='detail'),
    # /int:pk/ 는 해당 주소뒤에 글번호이며 글번호에 따라 다른내용이 만들어져서 안에 내용이 바뀜
    # 자동으로 만들어지면 int 숫자 값이다 이거임 <pk>로 두면 문자형식이 됨
    path("update/<int:pk>", BookmarkUpdateView.as_view(), name='update'),
    path("delete/<int:pk>", BookmarkDeleteView.as_view(), name='delete'),
]