from django.contrib import admin

# Register your models here.
from .models import Order , OrderDetail , Cart , CartDetail

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_code','order_status', 'order_date', 'delivery_date']
    list_filter  = ['order_status','order_date']

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['order','product',  'price', 'quantity', 'total']
    list_filter = ['price','quantity']

class CartAdmin(admin.ModelAdmin):
    list_display = ['user','cart_status']
    list_filter  = ['cart_status']

class CartDetailAdmin(admin.ModelAdmin):
    list_display = ['cart','product',  'price', 'quantity', 'total']
    list_filter = ['price','quantity']    

admin.site.register(Order,OrderAdmin )
admin.site.register(OrderDetail,OrderDetailAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(CartDetail,CartDetailAdmin)
  