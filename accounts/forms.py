from django.contrib.auth.models import User
from django import forms

# 폼: 폼태그 -> html의 태그인대 -> 프론트단에서 사용자의 입력을 받는 인터페이스 역할을 수행
# 장고의 폼은: html 의 폼 역할, 데이터 베이스에 저장할 내용을 어떤한 형식으로 , 제약조건을 만듬
class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']