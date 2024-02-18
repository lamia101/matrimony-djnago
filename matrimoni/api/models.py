# models.py
from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    permanent_address = models.CharField(max_length=255)
    current_address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    facebook_link = models.CharField(max_length=255)
    instagram_link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    gender = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    marital_status = models.CharField(max_length=255)
    account_for = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class GetInTouch(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.name
