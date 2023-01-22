from django.db import models

# Create your models here.

PRODUCT_FLAG = (
    ('Sale , Sales'),
    ('Feature' , 'Feature'),
    ('New' , 'New'),

class Product(models.Model):
    
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='posts/', default='default.png')
    flag = models.CharField(max_length=10,choices=PTODUCT_FLAG)
    price = models.FloatField()
    sku = models.IntegerField()
    brand = ''
    tags = ''
    subtitle = models.TextField(max_length=500)
    description = models.TextField(max_length=2000)
    '''
    name
    image
    flag
    price
    sku
    brand
    tags
    subtitle
    description
    '''







class ProductImages(models.Model):
    pass
    '''
    product,foreignkey
    image

    '''



class Brand(models.Model):
    pass
    '''
    name
    image
    '''


class Reviews(models.Model):
    pass        
    '''
    user
    product
    reviews
    date
    rate
    '''