from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from .models import Photo

@login_required
def photo_list(request):
    # 보여줄 사진 데이터 필요
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})

class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo','text'] #작성장(author), 작성시간(created) 있어야하지만 로그인해서 씀으로 자동처리됨 작성시간도 어떠한 동작때문에 자동으로 됨
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id # 규칙이다 외워라
        if form.is_valid():
            #데이터가 올바르다면 저장을 하겠다. photo 모델에 인스턴스가 존재하며 저장을하게됨
            form.instance.save()
            return redirect('/') # succes url 이 동작했어야되는게 이거임
        else:
            return self.render_to_response({'form':form})


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/update.html'


"""
서버에 이미지 파일을 업로하거나 수정하거나 지운다.
장고 웹 앱이 한다.
장고 웹 앱은 특정 서버에 업로드 되어 있다. 
* 그럼 해당 기능은 특정 서버 안에서만 영향을 끼칠수 있다.
-> 실 서비스를 배포하면 서버 컴퓨터는 1대가 아니다.
-> 사용자가 늘어날 떄마다 서버 컴퓨터도 늘어난다.
-> 장고 웹 앱이 업로드 되어있는 서버 컴퓨터가 늘어난다.
-> 이미지 파일이 업로도 되는 컴퓨터의 댓수도 늘어나야 한다.
-> 업로드 받은 후에 다른 서버에도 공유해줘야 한다.
-> 공유해주는데 사용되는 자원(돈이나 시간)이 아깝다.
-> 어떻게 하면 공유하는데 들어가는 돈이나 시간을 절약할 수 있을까?
-> 이미지는 한곳의 서버에다만 올려놓고, 거기에 접속해서 사용하자. 
"""
