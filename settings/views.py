from django.shortcuts import render
from product.models import Product , Brand , Reviews
from django.db.models import Count


# Create your views here.


def home(request):
    brands = Brand.objects.all().annotate(product_count=Count('product_brand'))
    items_sale = Product.objects.filter(flag='Sale')[:10]
    items_Feature = Product.objects.filter(flag='Feature')[:6]
    items_New = Product.objects.filter(flag='New')[:12]
    reviews = Reviews.objects.all()[:6]
    return render(request, 'settings/home.html',{'brands':brands ,'items_sale':items_sale, 'items_Feature':items_Feature, 'items_New':items_New,
    'reviews':reviews,
     })
    
