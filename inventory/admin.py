from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class SuperCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'image_preview')
    readonly_fields = ('image_preview',)
    list_filter = ('is_active',)
    search_fields = ('name',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" alt="{obj.name}" width="100" height="100"/>')
        else:
            return '(No image)'
        
    image_preview.short_description = 'Image Preview'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_super_categories')
    list_filter = ('super_category__name',)  # Use the correct field name
    search_fields = ('name',)

    def display_super_categories(self, obj):
        return ', '.join([sc.name for sc in obj.super_category.all()])

    display_super_categories.short_description = 'Super Categories'


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_categories')
    list_filter = ('category__name',)  # Use the correct field name
    search_fields = ('name',)

    def display_categories(self, obj):
        return ', '.join([cat.name for cat in obj.category.all()])

    display_categories.short_description = 'Categories'


admin.site.register(SuperCategory, SuperCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product)