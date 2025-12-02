from django.contrib import admin
from .models import Product, Variation


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'price', 'stock', 'is_available', 'category', 'modified_date')
    list_editable = ('price', 'stock', 'is_available')



class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'Variation_category', 'variation_value', 'is_active', 'created_date')
    list_editable = ('is_active',)
    list_filter = ('product', 'Variation_category', 'variation_value')
    
     


admin.site.register(Product, ProductAdmin)
admin.site.register (Variation, VariationAdmin)