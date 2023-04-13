from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/')

    code = models.CharField(max_length=8 , default=generate_code)

Number_Choices = (
    ('Primary', 'Primary'),
    ('Secondery', 'Secondery')
)


class ContactNumbers(models.Model):
    user = models.ForeignKey(User,related_query_name='user_contacts' ,on_delete=models.CASCADE) 
    type = models.CharField(max_length=10 , choices=Number_Choices)   
    number = models.CharField(max_length=20)

Address_Choices = (
   
    ('Home','Home'),
    ('Office','Office'),
    ('Bussiness','Bussiness'),
    ('Academy','Academy'),
    ('Others','Othres')
)


class Address(models.Model):
    user = models.ForeignKey(User,related_query_name='user_address' ,on_delete=models.CASCADE) 
    type = models.CharField(max_length=10 , choices=Address_Choices)
    city = models.CharField( max_length=20)
    street = models.CharField( max_length=20)
    house = models.CharField( max_length=20)
    notes = models.CharField( max_length=200)