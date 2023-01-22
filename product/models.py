from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

PRODUCT_FLAG = (
    ('Sale','Sales'),
    ('Feature','Feature'),
    ('New','New'),

class Product(models.Model):
    
    name = models.CharField(_('name'),max_length=150)
    image = models.ImageField(_('image'),upload_to='posts/', default='default.png')
    flag = models.CharField(_('flag')max_length=10,choices=PTODUCT_FLAG)
    price = models.FloatField(_('price'))
    sku = models.IntegerField(_('sku'))
    brand = models.ForeignKey('Brand', verbose_name=_('brand'), related_name='product_brand', on_delete=models.CASCADE)
    tags = TaggableManager()
    subtitle = models.TextField(_('subtitle'),max_length=500)
    description = models.TextField(_('description'),max_length=2000)
    slug = models.SlugField(null=True,blank=True)


    def__str__(self):
        return self.name
   


class ProductImages(models.Model):
    product = models.ForeignKey(Product,verbose_name=_('product') ,related_name='product_image',on_delete=models.CASCADE)
    image = models.ImageField(_('image')upload_to='product_images/')

    def __str__(self):
        return str(self.product)




class Brand(models.Model):
    name = models.CharField(_('brand'), max_length=50)
    image = models.ImageField(_('image')upload_to='brand/')
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