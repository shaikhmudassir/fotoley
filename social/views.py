from curses import use_default_colors
from django.views import View
from django.contrib.auth import get_user_model, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *

class Login(View):
    def get(self, request):
        if 'user_id' in request.session:
            return HttpResponseRedirect('')
        
        return render(request, 'social/login.html', {
        })

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(email=email, password=password)
        if user is not None:
            request.session['user_id'] = user.id
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('login')

class Register(View):
    def post(self, request, *args, **kwargs):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        username = email.split('@')[0]
        print(first_name, last_name)
        get_user_model().objects.create_user(email, username, password, first_name, last_name)
        
        return HttpResponseRedirect('login')	

class Home(View):
    def get(self, request):
        # Get all users list except self , render it
        # Get all the post of followed users

        user_id = request.session['user_id']
        users = User.objects.exclude(id=user_id).exclude(username='admin')
        print(users)
        return render(request, 'social/index.html', {
        })

class Logout(View):
    def get(self, request):
        try:
            del request.session['user_id']
            return HttpResponseRedirect('login')
        except KeyError as e:
            print(e)
            return HttpResponseRedirect('/')