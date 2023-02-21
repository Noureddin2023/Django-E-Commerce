from django.shortcuts import render , redirect
from django.views.generic import ListView , DetailView
from django.db.models import Count
from .models import Product , Brand , Reviews
from django.db.models import Q , F ,Value , Func , ExpressionWrapper , FloatField , DecimalField


from django.db.models.aggregates import Sum , Avg , Min , Max , Count
from django.db.models.functions import Concat
from .forms import ProductReviewForm
from django.http import JsonResponse
from django.template.loader import render_to_string
 
def query_Debug(request):
    #data = Product.objects.filter(name__contains='noah',price__gt=70)
    #data = Product.objects.filter(price=F('quantity'))
    #data = Product.objects.filter(Q(name__contains='noah') & Q(price__gt=70))  
    #data = Product.objects.filter(price__gt=70).order_by('name').reverse()
    #data = Product.objects.order_by('name')
    #data = Product.objects.select_related('brand').all()
    #data = Product.objects.prefetch_related('brand').all()## many to many
    #data = Product.objects.aggregate(min_price=Min('price'),avg_price=Avg('price'))
    
    #data = Product.objects.annotate(
        #full_name=Func(F('name'),F('flag'),function=('CONCAT')))

    #data = Product.objects.annotate(
        #full_name=Concat('name',Value(' '),'flag'))

    dis_price = ExpressionWrapper(F('price')*.8,output_field=DecimalField())

    data = Product.objects.annotate(discounted_price = dis_price)    
    


    return render(request,'product/productlist.html',{'data':data})


class ProductList(ListView):
    model = Product
    paginate_by = 50  


class ProductDetail(DetailView):
    model = Product 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Reviews.objects.filter(product=self.get_object())
        return context
    

        
def add_review(request,slug):
    product = Product.objects.get(slug=slug)
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.product = product 
            myform.save()

            reviews = Reviews.objects.filter(product=product)
            html = render_to_string('include/all_reviews.html',{'reviews':reviews , request:request})
            return JsonResponse({'result':html})
           # return redirect(f'/products/{product.slug}')

class BrandList(ListView):
    model = Brand
    paginate_by = 50
    queryset = Brand.objects.all().annotate(product_count=Count('product_brand'))
    

class BrandDetail(ListView):
    model = Product
    paginate_by = 50
    template_name = 'product/brand_detail.html'


    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(brand=brand)
        return queryset

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            #context["brand"] = Brand.objects.filter(slug=slug).annotate(product_count=Count('product_brand'))[0]
            data = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
            print(f"Brand : {data.name}")
            print(f"Brand : {data.image}")
            context["brand"] = data
            return context
