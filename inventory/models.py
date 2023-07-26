from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import uuid
# Create your models here.

#Model for the dropdown menu and stuff
class SuperCategory(models.Model):
    
    class Meta:
        verbose_name = '1 Super Category'
        verbose_name_plural = '1 Super Categories'
        
    name = models.CharField(max_length=100, help_text="Please write the name in ALL CAPITALS")
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='super_category/', null=True, blank=True, help_text="Please upload an image with dimensions 1080x1080.")

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Convert the name to uppercase before saving
        self.name = self.name.upper()
        super(SuperCategory, self).save(*args, **kwargs)


class Category(models.Model):
    
    class Meta:
        verbose_name = '2 Category'
        verbose_name_plural = '2 Categories'
        
    name = models.CharField(max_length=200)
    super_category = models.ManyToManyField(SuperCategory, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Convert the name to uppercase before saving
        self.name = self.name.upper()
        super(Category, self).save(*args, **kwargs)


class SubCategory(models.Model):
    
    class Meta:
        verbose_name = '3 Sub Category'
        verbose_name_plural = '3 Sub Categories'
        
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category, blank=True)
 
    def __str__(self):
        return self.name


#Model for the Circle Images and Stuff

class CircleCategory(models.Model):
    
    class Meta:
        verbose_name = 'Circle Category'
        verbose_name_plural = 'Circle Categories'
        
    circle_image = models.ImageField(upload_to='circle_category/', null=True, blank=True, help_text="Please upload an image with dimensions 1080x1080.")  # Assuming the image source is a URL with a maximum length of 200 characters.
    alt_text = models.CharField(max_length=100, help_text="Please provide the alternate tex to display")   # Assuming alt text has a maximum length of 100 characters.
    circle_category_name = models.CharField(max_length=50, help_text="This is the text that appears below the Circle")

    def __str__(self):
        return self.circle_category_name

class MainBanner(models.Model):
    
    class Meta:
        verbose_name = 'Main Banner'
        verbose_name_plural = 'Main Banners'
    
    image = models.ImageField(upload_to='banners/')
    alternate_text = models.CharField(max_length=255)
    active = models.BooleanField(default=False)

class SubBanner(models.Model):
    image = models.ImageField(upload_to='subbanner_images/')  
    alternate_text = models.CharField(max_length=255, null=True)
    active = models.BooleanField(default=False)

class MobileBanner(models.Model):
    image = models.ImageField(upload_to='mobilebanner_images/')  
    alternate_text = models.CharField(max_length=255, null=True)
    active = models.BooleanField(default=False)


class LeftImageContainer(models.Model):
    
    class Meta:
        verbose_name = 'Left Image Container'
        verbose_name_plural = 'Left Image Container'
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Left_Image_Container/Side_Banner/')
    alternate_text = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class LeftContainerSubImages(models.Model):
    
    class Meta:
        verbose_name = 'Left Container Sub Image'
        verbose_name_plural = 'Left Container Sub Images'
    
    container = models.ForeignKey(LeftImageContainer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Left_Image_Container/Sub_Images/')
    alternate_text = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)


class RightImageContainer(models.Model):
    
    class Meta:
        verbose_name = 'Right Image Container'
        verbose_name_plural = 'Right Image Container'
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Right_Image_Container/Side_Banner/')
    alternate_text = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class RightContainerSubImages(models.Model):
    
    class Meta:
        verbose_name = 'Right Container Sub Image'
        verbose_name_plural = 'Right Container Sub Images'
    
    container = models.ForeignKey(RightImageContainer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Right_Image_Container/Sub_Images/')
    alternate_text = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)







class Product(models.Model):
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    product_main_image = models.ImageField(upload_to='Product/MainImage/')
    sub_image1 = models.ImageField(upload_to='Product/SubImages/', blank=True)
    sub_image2 = models.ImageField(upload_to='Product/SubImages/', blank=True)
    sub_image3 = models.ImageField(upload_to='Product/SubImages/', blank=True)
    sub_image4 = models.ImageField(upload_to='Product/SubImages/', blank=True)
    sub_image5 = models.ImageField(upload_to='Product/SubImages/', blank=True)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    actual_price = models.DecimalField(max_digits=10, decimal_places=2)
    best_seller = models.BooleanField(default=False)
    description = models.JSONField(default=list)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    number_reviews = models.PositiveIntegerField(null=True)
    stock = models.CharField(max_length=20, default='100', null=True)
    SubCategory = models.ManyToManyField(SubCategory, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

import os

def get_image_upload_path(instance, filename):
    """
    Returns the upload path for the image file based on the model name
    """
    # Get the model name
    model_name = instance.__class__.__name__

    # Construct the upload path
    return os.path.join('dropdown_images', model_name, filename)
