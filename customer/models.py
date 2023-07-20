# from django.db import models

# # Create your models here.

# class User(models.Model):
#     full_name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     mobile_number = models.CharField(max_length=20)
#     password = models.CharField(max_length=255)

#     def __str__(self):
#         return self.full_name

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, full_name, mobile_number, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, mobile_number=mobile_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, mobile_number, password=None):
        user = self.create_user(email=email, full_name=full_name, mobile_number=mobile_number, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'mobile_number']

    objects = CustomUserManager()
