from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import uuid
# Create your models here.

#Model for the dropdown menu and stuff
class SuperCategory(models.Model):
    
    class Meta:
        verbose_name = 'Super Category'
        verbose_name_plural = 'Super Categories'
        
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
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
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
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'
        
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

class MainBanner(models.Model):
    image = models.ImageField(upload_to='banners/')
    alternate_text = models.CharField(max_length=255)
    active = models.BooleanField(default=False)






class Product(models.Model):
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    product_main_image = models.URLField()
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    actual_price = models.DecimalField(max_digits=10, decimal_places=2)
    best_seller = models.BooleanField(default=False)
    description = models.JSONField(default=list)  # Store description as a list of strings
    images = models.JSONField(default=list)  # Store multiple image URLs as a list
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    number_reviews = models.PositiveIntegerField()
    availability = models.CharField(max_length=20)
    super_category = models.ForeignKey(SuperCategory, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    SubCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.JSONField(default=list)  # If using Django version >= 3.1, otherwise use TextField
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
