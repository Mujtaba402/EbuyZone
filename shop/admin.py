from django.contrib import admin
from .models import product, Orders, Contact, OrderCome, Comment, OrderReceived


class ProductAdmin(admin.ModelAdmin):
    list_display        = ('product_name', 'category', 'price')
    list_filter         = ('category', 'pub_date')
    search_fields       = ('product_name', 'category', 'price')
    prepopulated_fields = {'subcategory':('category',)}
    date_hierarchy      = ('pub_date')

class OrdersAdmin(admin.ModelAdmin):
    list_display        = ('amount', 'name', 'email', 'address', 'phone', 'city')
    list_filter         = ('city',)
    search_fields       = ('name', 'email', 'address', 'phone', 'city')

class ContactAdmin(admin.ModelAdmin):
    list_display        = ('msg_id','name', 'email', 'phone','desc')
    search_fields       = ('name', 'email', 'phone')

class OrderComeAdmin(admin.ModelAdmin):
    list_display        = ('order_id', 'update_desc', 'timestamp')
    list_filter         = ('update_desc', 'timestamp')
    search_fields       = ('order_id', 'update_desc', 'timestamp')
    date_hierarchy      = ('timestamp')

class OrderReceivedAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'name', 'address', 'amount')
    search_fields = ('order_id', 'name', 'address')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'reply')
    search_fields = ('post', 'user')


admin.site.site_header = 'EBuyZone'
admin.site.register(product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderCome, OrderComeAdmin)
admin.site.register(OrderReceived, OrderReceivedAdmin)
admin.site.register(Comment, CommentAdmin)

