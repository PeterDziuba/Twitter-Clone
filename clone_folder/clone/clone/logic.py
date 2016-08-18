from . import models
import json
import random

def create_a_user(new_username, new_password, new_email):
    '''Creates a new user.'''
    new_user = models.User.objects.create_user(new_username,
                                               email=new_email,
                                               password=new_password)