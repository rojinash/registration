from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    form = request.POST
    errors_returned = User.objects.register_validator(form)
    # print(errors_returned)
    if len(errors_returned) > 0:
        request.session['register_error'] = True
        for single_error in errors_returned.values():
            messages.error(request, single_error)
        return redirect('/')
    hashed_pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
    new_user = User.objects.create(first_name=form['first_name'], last_name=form['last_name'], username=form['username'], email=form['email'], password=hashed_pw)
    request.session['user_id']=new_user.id
    return redirect('/homepage')

def login(request):
    form = request.POST
    login_errors = User.objects.login_validator(form)
    if len(login_errors) > 0:
        request.session['register_error'] = False
        for login_error in login_errors.values():
            messages.error(request, login_error)
        return redirect('/')
    user_id = User.objects.get(username=form['username']).id
    request.session['user_id'] = user_id    
    return redirect('/homepage')

def post_blogs(request):
    context = {
        'current_user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'post_blogs.html', context)

def process_blog(request):
    form = request.POST
    current_user = User.objects.get(id=request.session['user_id'])
    Blog.objects.create(title=form['title'], content=form['content'], created_by=current_user)
    return redirect('/post_blogs')

def homepage(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'blogs': Blog.objects.all(),
        'current_user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'homepage.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')