from django.contrib import admin
from .models import Category, Box, Product

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):

    filter_horizontal = ('category',)


admin.site.register(Category)
admin.site.register(Box, CategoryAdmin)
admin.site.register(Product)
