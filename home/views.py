from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')

@login_required(login_url='/login')
def index_english(request):
    return render(request, 'indexe.html')

@login_required(login_url='/login')
def index_hindi(request):
    return render(request, 'index-H.html')

@login_required(login_url='/login')
def index_korean(request):
    return render(request, 'index-K.html')

def handle_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"] 
        user  = authenticate(username = username, password  = password)
        if user is not None:
            login(request, user)
            return redirect("ask_lang")
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

def do_logout(request):
    logout(request)
    return redirect('/login')

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"] 
        cpassword = request.POST["cpassword"]

        if password == cpassword:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return render(request, 'asklang')
        return render(request, 'login.html')
    return render(request, 'login.html')

def ask_lang(request):
    return render(request, 'lang.html')