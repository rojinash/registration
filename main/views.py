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
        for single_error in errors_returned.values():
            messages.error(request, single_error)
        return redirect('/')
    hashed_pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
    new_user = User.objects.create(first_name=form['first_name'], last_name=form['last_name'], username=form['username'], email=form['email'], password=hashed_pw)
    return redirect('/')