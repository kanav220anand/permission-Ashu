import uuid

from django.contrib.auth.models import AbstractBaseUser, UserManager, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.db import models

# Create your models here.


class MyAccountManager(BaseUserManager):

    def create_superuser(self, email, password):
        user = User.objects.create(
            email=email
        )
        user.is_admin =True
        user.is_staff =True
        user.is_active = True
        user.is_superuser=True
        user.user_type = User.SUPERUSER

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    MANAGER = "MANAGER"
    CUSTOMER = "CUSTOMER"
    SUPERUSER = "SUPERUSER"

    USER_TYPES = [(MANAGER, "MANAGER"), (CUSTOMER, "CUSTOMER"), (SUPERUSER, "SUPERUSER")]

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    user_type = models.CharField(max_length=30, choices=USER_TYPES)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    date_joined = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    objects = MyAccountManager()

    class Meta:
        ordering = ("email",)
