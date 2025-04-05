from unittest.util import _MAX_LENGTH
from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

class ChatBot(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_box =  models.TextField(null=True, blank=True)
    chat_response = models.TextField(null=True, blank=True)
    
