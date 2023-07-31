from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import uuid
import boto3
from botocore.exceptions import NoCredentialsError
from django.conf import settings as conf_settings
import os
from django.core.exceptions import ValidationError
# Create your models here.

#Model for the dropdown menu and stuff
class SuperCategory(models.Model):
    
    class Meta:
        verbose_name = '1 Super Category'
        verbose_name_plural = '1 Super Categories'
        
    name = models.CharField(max_length=100, help_text="Please write the name in ALL CAPITALS")
    is_active = models.BooleanField(default=True)
    image = models.ImageField( null=True, blank=True, help_text="Please upload an image with dimensions 1080x1080.")

    def __str__(self):
        return self.name
    
    #Aws code to upload images     
    def save(self, *args, **kwargs):
        self.name = self.name.upper()

        if self.image and self._state.adding:
            try:
                s3 = boto3.client('s3', aws_access_key_id=conf_settings.AWS_ACCESS_KEY,
                                  aws_secret_access_key=conf_settings.AWS_SECRET_ACCESS_KEY,
                                  region_name=conf_settings.AWS_REGION)

                folder_name = self.__class__.__name__  
                image_key = f'{folder_name}/{os.path.basename(self.image.name)}'

                s3.upload_fileobj(self.image, conf_settings.AWS_STORAGE_BUCKET_NAME, image_key)
                self.image = f'https://joyful-bucket.s3.ap-south-1.amazonaws.com/{image_key}'
            except NoCredentialsError as e:
                raise ValidationError(f"AWS S3 credentials are not set up properly: {e}")

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
    super_categories = models.ManyToManyField(SuperCategory)
 
    def __str__(self):
        return self.name


#Model for the Circle Images and Stuff

class CircleCategory(models.Model):
    
    class Meta:
        verbose_name = '4 Circle Category'
        verbose_name_plural = '4 Circle Categories'
        
    circle_image = models.ImageField( null=True, blank=True, help_text="Please upload an image with dimensions 1080x1080.") 
    alt_text = models.CharField(max_length=100, help_text="Please provide the alternate tex to display")
    circle_category_name = models.CharField(max_length=50, help_text="This is the text that appears below the Circle")

    def __str__(self):
        return self.circle_category_name
    
    def save(self, *args, **kwargs):
        if self.circle_image and self._state.adding:
            try:
                s3 = boto3.client('s3', aws_access_key_id=conf_settings.AWS_ACCESS_KEY,
                                  aws_secret_access_key=conf_settings.AWS_SECRET_ACCESS_KEY,
                                  region_name=conf_settings.AWS_REGION)

                folder_name = self.__class__.__name__
                image_key = f'{folder_name}/{os.path.basename(self.circle_image.name)}'

                s3.upload_fileobj(self.circle_image, conf_settings.AWS_STORAGE_BUCKET_NAME, image_key)
                self.circle_image = f'https://joyful-bucket.s3.ap-south-1.amazonaws.com/{image_key}'
            except NoCredentialsError as e:
                raise ValidationError(f"AWS S3 credentials are not set up properly: {e}")

        super(CircleCategory, self).save(*args, **kwargs)

class MainBanner(models.Model):
    
    class Meta:
        verbose_name = '5 Main Banner'
        verbose_name_plural = '5 Main Banners'
    
    image = models.ImageField()
    alternate_text = models.CharField(max_length=255)
    active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.image and self._state.adding:
            try:
                s3 = boto3.client('s3', aws_access_key_id=conf_settings.AWS_ACCESS_KEY,
                                  aws_secret_access_key=conf_settings.AWS_SECRET_ACCESS_KEY,
                                  region_name=conf_settings.AWS_REGION)

                folder_name = self.__class__.__name__
                image_key = f'{folder_name}/{os.path.basename(self.image.name)}'

                s3.upload_fileobj(self.image, conf_settings.AWS_STORAGE_BUCKET_NAME, image_key)
                self.image = f'https://joyful-bucket.s3.ap-south-1.amazonaws.com/{image_key}'
            except NoCredentialsError as e:
                raise ValidationError(f"AWS S3 credentials are not set up properly: {e}")

        super(MainBanner, self).save(*args, **kwargs)


class SubBanner(models.Model):
    class Meta:
        verbose_name = '6 SubBanner'
        verbose_name_plural = '6 SubBanners'
    image = models.ImageField()  
    alternate_text = models.CharField(max_length=255, null=True)
    active = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if self.image and self._state.adding:
            try:
                s3 = boto3.client('s3', aws_access_key_id=conf_settings.AWS_ACCESS_KEY,
                                  aws_secret_access_key=conf_settings.AWS_SECRET_ACCESS_KEY,
                                  region_name=conf_settings.AWS_REGION)

                folder_name = self.__class__.__name__
                image_key = f'{folder_name}/{os.path.basename(self.image.name)}'

                s3.upload_fileobj(self.image, conf_settings.AWS_STORAGE_BUCKET_NAME, image_key)
                self.image = f'https://joyful-bucket.s3.ap-south-1.amazonaws.com/{image_key}'
            except NoCredentialsError as e:
                raise ValidationError(f"AWS S3 credentials are not set up properly: {e}")

        super(SubBanner, self).save(*args, **kwargs)

class MobileBanner(models.Model):
    class Meta:
        verbose_name = '7 MobileBanner'
        verbose_name_plural = '7 MobileBanners'
    image = models.ImageField()  
    alternate_text = models.CharField(max_length=255, null=True)
    active = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if self.image and self._state.adding:
            try:
                s3 = boto3.client('s3', aws_access_key_id=conf_settings.AWS_ACCESS_KEY,
                                  aws_secret_access_key=conf_settings.AWS_SECRET_ACCESS_KEY,
                                  region_name=conf_settings.AWS_REGION)

                folder_name = self.__class__.__name__
                image_key = f'{folder_name}/{os.path.basename(self.image.name)}'

                s3.upload_fileobj(self.image, conf_settings.AWS_STORAGE_BUCKET_NAME, image_key)
                self.image = f'https://joyful-bucket.s3.ap-south-1.amazonaws.com/{image_key}'
            except NoCredentialsError as e:
                raise ValidationError(f"AWS S3 credentials are not set up properly: {e}")

        super(MobileBanner, self).save(*args, **kwargs)


class LeftImageContainer(models.Model):
    
    class Meta:
        verbose_name = '8 Left Image Container'
        verbose_name_plural = '8 Left Image Container'
    
    name = models.CharField(max_length=100)
    image = models.ImageField()
    alternate_text = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.image and self._state.adding:
            try:
                s3 = boto3.client('s3', aws_access_key_id=conf_settings.AWS_ACCESS_KEY,
                                  aws_secret_access_key=conf_settings.AWS_SECRET_ACCESS_KEY,
                                  region_name=conf_settings.AWS_REGION)

                folder_name = self.__class__.__name__
                image_key = f'{folder_name}/{os.path.basename(self.image.name)}'

                s3.upload_fileobj(self.image, conf_settings.AWS_STORAGE_BUCKET_NAME, image_key)
                self.image = f'https://joyful-bucket.s3.ap-south-1.amazonaws.com/{image_key}'
            except NoCredentialsError as e:
                raise ValidationError(f"AWS S3 credentials are not set up properly: {e}")

        super(LeftImageContainer, self).save(*args, **kwargs)

class LeftContainerSubImages(models.Model):
    
    class Meta:
        verbose_name = '9 Left Container Sub Image'
        verbose_name_plural = '9 Left Container Sub Images'
    
    container = models.ForeignKey(LeftImageContainer, on_delete=models.CASCADE)
    image = models.ImageField()
    alternate_text = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if self.image and self._state.adding:
            try:
                s3 = boto3.client('s3', aws_access_key_id=conf_settings.AWS_ACCESS_KEY,
                                  aws_secret_access_key=conf_settings.AWS_SECRET_ACCESS_KEY,
                                  region_name=conf_settings.AWS_REGION)

                folder_name = self.__class__.__name__
                image_key = f'{folder_name}/{os.path.basename(self.image.name)}'

                s3.upload_fileobj(self.image, conf_settings.AWS_STORAGE_BUCKET_NAME, image_key)
                self.image = f'https://joyful-bucket.s3.ap-south-1.amazonaws.com/{image_key}'
            except NoCredentialsError as e:
                raise ValidationError(f"AWS S3 credentials are not set up properly: {e}")

        super(LeftContainerSubImages, self).save(*args, **kwargs)


class RightImageContainer(models.Model):
    
    class Meta:
        verbose_name = '10 Right Image Container'
        verbose_name_plural = '10 Right Image Container'
    
    name = models.CharField(max_length=100)
    image = models.ImageField()
    alternate_text = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.image and self._state.adding:
            try:
                s3 = boto3.client('s3', aws_access_key_id=conf_settings.AWS_ACCESS_KEY,
                                  aws_secret_access_key=conf_settings.AWS_SECRET_ACCESS_KEY,
                                  region_name=conf_settings.AWS_REGION)

                folder_name = self.__class__.__name__
                image_key = f'{folder_name}/{os.path.basename(self.image.name)}'

                s3.upload_fileobj(self.image, conf_settings.AWS_STORAGE_BUCKET_NAME, image_key)
                self.image = f'https://joyful-bucket.s3.ap-south-1.amazonaws.com/{image_key}'
            except NoCredentialsError as e:
                raise ValidationError(f"AWS S3 credentials are not set up properly: {e}")

        super(RightImageContainer, self).save(*args, **kwargs)

class RightContainerSubImages(models.Model):
    
    class Meta:
        verbose_name = '11 Right Container Sub Image'
        verbose_name_plural = '11 Right Container Sub Images'
    
    container = models.ForeignKey(RightImageContainer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Right_Image_Container/Sub_Images/')
    alternate_text = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.image and self._state.adding:
            try:
                s3 = boto3.client('s3', aws_access_key_id=conf_settings.AWS_ACCESS_KEY,
                                  aws_secret_access_key=conf_settings.AWS_SECRET_ACCESS_KEY,
                                  region_name=conf_settings.AWS_REGION)

                folder_name = self.__class__.__name__
                image_key = f'{folder_name}/{os.path.basename(self.image.name)}'

                s3.upload_fileobj(self.image, conf_settings.AWS_STORAGE_BUCKET_NAME, image_key)
                self.image = f'https://joyful-bucket.s3.ap-south-1.amazonaws.com/{image_key}'
            except NoCredentialsError as e:
                raise ValidationError(f"AWS S3 credentials are not set up properly: {e}")

        super(RightContainerSubImages, self).save(*args, **kwargs)


class Product(models.Model):
    
    class Meta:
        verbose_name = '12 Product'
        verbose_name_plural = '12 Products'
        
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    product_main_image = models.ImageField(upload_to='Product/MainImage/')
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    actual_price = models.DecimalField(max_digits=10, decimal_places=2)
    best_seller = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    number_reviews = models.PositiveIntegerField(null=True, blank=True)
    stock = models.CharField(max_length=20, default='100', null=True)
    SubCategory = models.ManyToManyField(SubCategory, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProductTag(models.Model):
    CHOICES = [
        ('text', 'Text'),
        ('date_picker', 'Date Picker'),
        ('image', 'Image'),
        ('multiple_images', 'Multiple Images'),
        # Add more choices as needed
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='tagsmain')
    tagname = models.CharField(max_length=100)
    tag = models.CharField(max_length=100, choices=CHOICES)
    has_color = models.BooleanField(default=False)

    def __str__(self):
        return self.tagname


class ProductTagEntry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='tags')
    tag = models.ForeignKey(ProductTag, on_delete=models.CASCADE)
    custom_tagname = models.CharField(max_length=100)
    custom_choice = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.product} - {self.custom_tagname}: {self.custom_choice}"

    
class ProductSubImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sub_images')
    sub_image1 = models.ImageField(upload_to='Product/SubImages/', blank=True)
    sub_image2 = models.ImageField(upload_to='Product/SubImages/', blank=True)
    sub_image3 = models.ImageField(upload_to='Product/SubImages/', blank=True)
    sub_image4 = models.ImageField(upload_to='Product/SubImages/', blank=True)
    sub_image5 = models.ImageField(upload_to='Product/SubImages/', blank=True)

    def __str__(self):
        return f"{self.product.name} - Sub-Images"
 
class ProductDescription(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='descriptions')
    heading1 = models.CharField(max_length=200, blank=True)
    text1 = models.TextField(blank=True)
    subheadingd1 = models.CharField(max_length=200, blank=True)
    subheadingd1_text = models.TextField(blank=True)
    subheadingd2 = models.CharField(max_length=200, blank=True)
    subheadingd2_text = models.TextField(blank=True)
    heading2 = models.CharField(max_length=200, blank=True)
    subheadingdi1 = models.CharField(max_length=200, blank=True)
    subheadingdi1_text = models.TextField(blank=True)
    heading3 = models.CharField(max_length=200, blank=True)
    subheadingi1 = models.CharField(max_length=200, blank=True)
    subheadingi1_text = models.TextField(blank=True)

    def __str__(self):
        return f"{self.product.name} - Product Description"

