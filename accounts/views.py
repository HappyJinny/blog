from django.shortcuts import render, redirect
from django.contrib import messages
#계정 권한
from django.contrib.auth.models import User 
from django.contrib import auth
from django.db import IntegrityError

# Create your views here.

def signup(request, backend='django.contrib.auth.backends.ModelBackend'):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                messages.warning(request, '이미 존재하는 회원입니다.')
                return render(request, 'signup.html')
            except User.DoesNotExist:
                user = User.objects.create_user( 
                    request.POST['username'], 
                    password=request.POST['password1']
                )
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, '회원가입 완료!')
                return redirect('home')
        else :
            messages.warning(request, '비밀번호가 맞지 않습니다.')
            return render (request, 'signup.html')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method =="POST":
        auth.logout(request)
        return redirect('home')
    return render(request, 'signup.html')


