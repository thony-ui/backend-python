from typing import Text
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

def home(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.is_true = True
    feature1.details = 'Our Service is Very Quick'

    feature2 = Feature()
    feature2.id = 0
    feature2.name = 'Fast'
    feature2.is_true = True
    feature2.details = 'Our Service is Very'

    feature3 = Feature()
    feature3.id = 0
    feature3.name = 'Fast'
    feature3.is_true = False
    feature3.details = 'Our Service is Very Quick'

    features2 = [feature1, feature2, feature3]

    features = Feature.objects.all()
   
    return render(request, 'index2.html', {'features':features})


def portfolio(request):
    context = {
        'name': 'thony',
        'age': 23,
        'nationality': 'British',
    }
    return render(request, 'portfolio.html', context)

def home2(request):
    return render(request, 'index3.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password = password)
                user.save()
                return redirect('/login')
        else:
            messages.info(request, 'Password is not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else: 
            messages.info(request,'Credentials invalid')
            return redirect('/login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    posts = ['tim','yom','lol']
    return render(request, "counter.html", {'posts':posts})

def post(request, pk):
    return render(request, 'post.html', {'pk':pk})

def portfolio(request):
    return render(request, 'portfolio.html')
	