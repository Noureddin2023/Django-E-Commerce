from django.db import models

# Create your models here.

class Product(models.Model):
    pass
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