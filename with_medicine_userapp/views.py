from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import auth
from .models import CustomUser
from django.contrib.auth import update_session_auth_hash  # 비밀번호 변경 시 로그아웃 되지 않도록
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)  # 회원가입 후 바로 로그인?
            return redirect('main')        
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form' : form})
    
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('main')
        else:
            return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form' : form})
    
def logout(request):
    auth.logout(request)
    return redirect('main')

def user_detail(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    return render(request, 'user_detail.html', {'user' : user})

def user_update(request):
    # form = None  # else 밖에서도 form을 사용하기 위해서
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('main') ##
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'user_update.html', {'form':form})

def user_delete(request):
    user = request.user
    user.delete()
    return redirect('main')

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            #update_session_auth_hash(request, form.user) # 비밀번호 변경 시 로그아웃 되지 않도록 session을 새로 만들지 않고 기존 테이블에 수정하는 함수
            return redirect('main')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form':form})
