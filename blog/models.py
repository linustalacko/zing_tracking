from django.db import models
from django.forms import CharField, PasswordInput

class Login(models.Model):
    username = CharField(max_length=42, min_length=42)
    password = PasswordInput()