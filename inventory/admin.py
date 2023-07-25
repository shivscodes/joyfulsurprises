from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class SuperCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'image_preview')
    readonly_fields = ('image_preview',)
    list_filter = ('is_active',)
    search_fields = ('name',)
    app_label = 'Custom Categories'

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

class CircleCategoryAdmin(admin.ModelAdmin):
    list_display = ('circle_image_preview', 'alt_text', 'circle_category_name')
    readonly_fields = ('circle_image_preview',)

    def circle_image_preview(self, obj):
        if obj.circle_image:
            return mark_safe(f'<img src="{obj.circle_image.url}" alt="{obj.alt_text}" width="100" height="100"/>')
        else:
            return 'No Image'
    circle_image_preview.allow_tags = True
    circle_image_preview.short_description = 'Circle Image Preview'
    
class BannerAdmin(admin.ModelAdmin):
    list_display = ('banner_image_preview', 'alternate_text', 'active')
    readonly_fields = ('banner_image_preview',)

    def banner_image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" alt="{obj.alternate_text}" width="200" height="100"/>')
        else:
            return 'No Image'

    banner_image_preview.allow_tags = True
    banner_image_preview.short_description = 'Banner Image Preview'


class SubBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'active')
    list_filter = ('active',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" alt="SubBanner {obj.id}" width="500" height="100"/>')
        else:
            return 'No Image'

    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'

class MobileBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'active')
    list_filter = ('active',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" alt="SubBanner {obj.id}" width="550" height="100"/>')
        else:
            return 'No Image'

    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'


    
class LeftImageContainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview', 'is_active')
    list_filter = ('name','is_active',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" alt="{obj.name}" width="100" height="150"/>')
        else:
            return 'No Image'

    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'
    
    
class LeftContainerSubImagesAdmin(admin.ModelAdmin):
    list_display = ('container', 'title', 'image_preview', 'is_active')
    list_filter = ('container', 'title', 'is_active')

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" alt="{obj.title}" width="100" height="100"/>')
        else:
            return 'No Image'

    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'


class RightImageContainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview', 'is_active')
    list_filter = ('name','is_active',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" alt="{obj.name}" width="100" height="150"/>')
        else:
            return 'No Image'

    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'

class RightContainerSubImagesAdmin(admin.ModelAdmin):
    list_display = ('container', 'title', 'image_preview', 'is_active')
    list_filter = ('container', 'title', 'is_active')

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" alt="{obj.title}" width="100" height="100"/>')
        else:
            return 'No Image'

    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'


admin.site.register(SuperCategory, SuperCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(CircleCategory, CircleCategoryAdmin)
admin.site.register(MainBanner,BannerAdmin)
admin.site.register(SubBanner,SubBannerAdmin)
admin.site.register(MobileBanner,MobileBannerAdmin)
admin.site.register(LeftImageContainer, LeftImageContainerAdmin)
admin.site.register(LeftContainerSubImages, LeftContainerSubImagesAdmin)
admin.site.register(RightImageContainer, RightImageContainerAdmin)
admin.site.register(RightContainerSubImages, RightContainerSubImagesAdmin)
admin.site.register(Product)