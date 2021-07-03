from django.db import models

# Create your models here.

class Contact(models.Model):
    _id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,blank=False)
    firstname = models.CharField(max_length=100,blank=False)
    email = models.CharField(max_length=100,blank=False)
    phone = models.CharField(max_length=50,blank=False)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Users(models.Model):
    _id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,blank=False)
    firstname = models.CharField(max_length=100,blank=False)
    lastname = models.CharField(max_length=100,blank=False)
    email = models.CharField(max_length=100,blank=False)
    password = models.CharField(max_length=100,blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
