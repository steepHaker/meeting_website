# meeting_create_user/models.py
from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from ckeditor.fields import RichTextField

class User(AbstractUser):
    userinfo = models.OneToOneField('UserInfo', null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default="")
    email = models.EmailField(max_length=50, default="")
    password = models.CharField(max_length=20, default="")
    repeatepassword = models.CharField(max_length=20, default="")
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='meeting_create_user',
        help_text='Specific permissions for the user.',
        related_query_name='meeting_create_user',
    )


class City(models.Model):
    citi = models.CharField(max_length=20, default="", null=True)

    def __str__(self):
        return self.citi

class Country(models.Model):
    country = models.CharField(max_length=20, default="", null=True)

    def __str__(self):
        return self.country

class Gender(models.Model):
    gender = models.CharField(max_length=20, default="", null=True)
    
    def __str__(self):
        return self.gender
    
class Horoscope(models.Model):
    horoscope = models.CharField(max_length=20, default="", null=True)
    
    def __str__(self):
        return self.horoscope
    
class Smoking(models.Model):
    smoking = models.CharField(max_length=20, default="", null=True)
    
    def __str__(self):
        return self.smoking
    
class Alcohol(models.Model):
    alcohol = models.CharField(max_length=25, default="", null=True)
    
    def __str__(self):
        return self.alcohol
    
class Children(models.Model):
    children = models.CharField(max_length=20, default="", null=True)
    
    def __str__(self):
        return self.children
    
class Pets(models.Model):
    favoritepets = models.CharField(max_length=20, default="", null=True)
    
    def __str__(self):
        return self.favoritepets
    
class Ethnicity(models.Model):
    ethnicity = models.CharField(max_length=20, default="", null=True)
    
    def __str__(self):
        return self.ethnicity
    
class UserInfo(models.Model):
    myuser = models.OneToOneField(User, on_delete=models.CASCADE, related_name='myuserinfo', blank=True, null=True, unique=True)
    nikname = models.CharField(max_length=20, default="", null=True)
    image = models.FileField(upload_to='user_image', default="")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    ethnicity = models.ForeignKey(Ethnicity, on_delete=models.CASCADE, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    age = models.IntegerField(null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    smoking = models.ForeignKey(Smoking, on_delete=models.CASCADE, blank=True,  null=True)
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE, blank=True,  null=True)
    children = models.ForeignKey(Children, on_delete=models.CASCADE, blank=True,  null=True)
    horoscope = models.ForeignKey(Horoscope, on_delete=models.CASCADE, blank=True,  null=True)
    
    favoritepets = models.CharField(max_length=20, blank=True, default="")
    favoritebooks = models.CharField(max_length=20, blank=True, default="")
    favoritefilms = models.CharField(max_length=20, blank=True, default="")
    favoritemusic = models.CharField(max_length=20, blank=True, default="")    
    interests = models.CharField(max_length=20, blank=True, default="")
    aboutme = RichTextField(default="")

    def __str__(self):
        return self.nikname

class Convertation(models.Model):
    partipants = models.ManyToManyField(User)

class Message(models.Model):
    convertation = models.ForeignKey(Convertation, on_delete=models.CASCADE, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(default="")
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="maessage_image")

