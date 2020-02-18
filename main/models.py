from django.db import models
import re


# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, post_data):
        user_errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_data['first_name']) < 2:
            user_errors['first_name'] = 'Please enter a longer first name'
        if len(post_data['last_name']) < 2:
            user_errors['last_name'] = 'Please enter a longer last name'
        all_user = User.objects.filter(username=post_data['username'])
        if len(all_user)>0:
            user_errors['duplicate_username'] = 'That username is already taken. Please choose another one'
        if len(post_data['username']) < 6:
            user_errors['username'] = 'Please enter a longer username'
        if not EMAIL_REGEX.match(post_data['email']):
            user_errors['email'] = "Invalid email address!"
        if len(post_data['password'])<6:
            user_errors['password'] = 'Please enter a longer password'
        if post_data['password']!=post_data['confirm_pw']:
            user_errors['confirm'] = 'Your passwords do not match. Try again'
        
        return user_errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

