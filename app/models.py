from django.db import models

# Create your models here.

class UserData(models.Model):
    Firstname = models.CharField(max_length=40);
    Lastname = models.CharField(max_length=40);
    Email = models.EmailField(max_length=40);
    Contact = models.CharField(max_length=40);
    Password = models.CharField(max_length=40);

class ContactForm(models.Model):
    Name = models.CharField(max_length=40);
    Email = models.EmailField(max_length=40);
    Contact = models.CharField(max_length=40);
    Message = models.CharField(max_length=150);