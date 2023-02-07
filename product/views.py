from django.shortcuts import render
from django.views.generic import ListView , DetailView
from django.db.models import Count
from .models import Product , Brand


class ProductList(ListView):
    model = Product
    paginate_by = 50


class ProductDetail(DetailView):
    model = Product


class BrandList(ListView):
    model = Brand
    paginate_by = 50
    queryset = Brand.objects.all().annotate(product_count=Count('product_brand'))
    

class BrandDetail(DetailView):
    model = Brand

    def get_queryset(self):
        queryset = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))
        return queryset