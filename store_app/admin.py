from django.contrib import admin
from .models import *



class Imagestublerinline(admin.TabularInline):
    model = Images

class Tagstublerinline(admin.TabularInline):
    model = Tag

class ProductAdmin(admin.ModelAdmin):
    inlines = [Imagestublerinline,Tagstublerinline]

class OrderItemtublerinline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemtublerinline]
    list_display = ['user','phone','email','paid','date']



admin.site.register(Images)
admin.site.register(Tag)
admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Product,ProductAdmin)
admin.site.register(Contact_us)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)