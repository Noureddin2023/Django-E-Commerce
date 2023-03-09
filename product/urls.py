from django.urls import path

app_name = 'product'


from .views import ProductList,ProductDetail,BrandList,BrandDetail,query_Debug , add_review
from .api import productlist_api , ProductListApi , ProductDetailApi , BrandDetailApi , BrandListApi

urlpatterns = [
    path('debug', query_Debug,name='qyery_debug'),
    path('', ProductList.as_view(),name='product_list'),
    path('<slug:slug>' , ProductDetail.as_view() , name='product_detail'),
    path('<slug:slug>/add-review', add_review , name='add_review'),
    path('brands/' , BrandList.as_view() , name='brand_list'),
    path('brands/<slug:slug>', BrandDetail.as_view() , name='brand_detail'),
    


    # api urls
    #path('api/list' , productlist_api , name='product list'),
    path('api/list' , ProductListApi.as_view() , name='product list'),
    path('api/list/brands' , BrandListApi.as_view() , name='brand list'),
    path('api/list/brands/<slug:slug>' , BrandDetailApi.as_view() , name='brand detail'),
    path('api/list/<slug:slug>' , ProductDetailApi.as_view() , name='product detail'),
   
]
    
 