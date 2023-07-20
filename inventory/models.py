from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os
# Create your models here.

#Image Upload Path
def get_image_upload_path(instance, filename):
    """
    Returns the upload path for the image file based on the category
    """
    # Get the category name
    category_name = instance.category.name

    # Construct the upload path
    return os.path.join('inventory_images', category_name, filename)

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Caterogies"
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    class Meta:
        verbose_name_plural = "Inventories"

    product_id = models.CharField(max_length=64, blank=True)
    caption = models.CharField(max_length=500, blank=True)
    actual_price = models.IntegerField(blank=True)
    discount_price = models.IntegerField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    offer = models.CharField(max_length=500, blank=True)
    images = models.ImageField(upload_to=get_image_upload_path, blank=True)
    is_in_stock = models.BooleanField(default=True)

    def __str__(self):
        return "{}-{}".format(self.product_id, self.caption)

@receiver(pre_delete, sender=Inventory)
def inventory_image_delete(sender, instance, **kwargs):
    """
    Deletes associated image file from filesystem
    when Inventory object is deleted.
    """
    # Get the image path
    image_path = instance.images.path

    # Check if the file exists and delete it
    if os.path.isfile(image_path):
        os.remove(image_path)