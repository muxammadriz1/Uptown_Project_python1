from django.db import models

# Create your models here.

class Service(models.Model):
    nomi = models.CharField(max_length=50)
    manzili = models.CharField(max_length=100)
    old_price = models.IntegerField()
    new_price = models.IntegerField()
    rooms = models.IntegerField()
    bath_rooms = models.IntegerField()
    maydon = models.FloatField()
    rasm = models.ImageField(upload_to='media')
    vaqt = models.DateTimeField(auto_now=True)


class Clients(models.Model):
    ismi = models.CharField(max_length=50)
    fam = models.CharField(max_length=50)
    malumot = models.CharField(max_length=800)
    rasmi = models.ImageField(upload_to='media')



class Agents(models.Model):
    ismi = models.CharField(max_length=50)
    fami = models.CharField(max_length=50)
    lavozimi = models.CharField(max_length=200)
    rasm = models.ImageField(upload_to='media')


class Blogs(models.Model):
    nomi = models.CharField(max_length=50)
    maydoni = models.FloatField()
    malumot = models.CharField(max_length=800)
    rasm = models.ImageField(upload_to='media')
    vaqt = models.DateTimeField(auto_now=True)


class Murojat(models.Model):
    ism = models.CharField(max_length=200)
    mail = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    massage = models.TextField()
    vaqt = models.DateTimeField(auto_now=True)
