from django.contrib import admin
from myapp.models import *
# Register your models here.

@admin.register(cart)
class cartAdmin(admin.ModelAdmin):
    list_display = ['id','customer','product','quantity']

@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ['id','name','section','price','is_rare','is_DrawTool']
    
@admin.register(customer)
class customerAdmin(admin.ModelAdmin):
    list_display = ['id','name','address','phone','email']
    
@admin.register(order)
class orderAdmin(admin.ModelAdmin):
    list_display = ['id','customer','product','quantity', 'date']