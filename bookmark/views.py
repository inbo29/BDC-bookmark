from django.shortcuts import render

# Create your views here.
# CRUD : Create, Read, Update, Delete
# List

# 클래스형 뷰, 함수형 뷰
# 클래형 쓸떄 제네릿을 쓴다
# 함수형은 제멋대로 하고싶을떄

# 웹 페이지에 접속한다 -> 페이지를 본다.
# URL을 입력 -> 웹 서버가 뷰를 찾아서 동작시킨다. -> 응답

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy       # url 패턴을 가지고 url 을 만들어줌
from django.views.generic.detail import DetailView
from .models import Bookmark

def home(request):
    return render(request, "bookmark/index.html")


class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateVeiw(CreateView):
    model = Bookmark
    fields = ['site_name', 'url'] # all이라는 경우도 있음 다 바꾼다는것이며 필드는 지정해서 바꾼다는 뜻
    success_url = reverse_lazy('list') # urls.py 중에 선택해라 하는뜻 지금은 네임 스페이스 안써서 기록한것만햇으며 나중에 하게됨
    template_name_suffix = '_create'
    # 모델들중에 그냥 뷰가 있으며 그건 굳이 모델로 지정안해줘도 됨
    # 기본적으로 업데이트랑 크리에이트는 뒤에 폼이 붙게되있음 왜냐 입력 받으면 수정해야되니깡 서픽스옵션은 뒤에 이름을 바꾸는것

class BookmarkDetailVeiw(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url'] # 어떤정보를 수정할것이냐 지정해줌
    template_name_suffix = '_update' # 기본적으로 _form을 불러오니깡 설정을 바꿔줘야함

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
    # 목록으로 돌아가 리스트를 불러와라 점검할떄 오류가 뜰수 있으므로 걍 리버스 말고 리버스 레이지 씀
    # delete에 경우 석세스 url 필요 삭제할경우로 어디론가 이동해야함