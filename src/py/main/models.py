from unicodedata import name
from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=500)

class username(models.Model):
    name = models.ForeignKey(Users, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text

class passwords(models.Model):
    password = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.text