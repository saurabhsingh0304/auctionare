from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class VendorUser(AbstractBaseUser, PermissionsMixin):
    COUNTRY_CHOICES = (('America', 'america'),
                       ('Germany', 'germany'),
                       ('Australia', 'australia'),
                       ('France', 'france'),)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(_('email address'),unique=True)
    email1 = models.EmailField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    company_name = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    telephone = models.IntegerField(default=0,blank=True)
    address1 = models.TextField(max_length=20)
    address2 =models.TextField(max_length=20, blank=True)
    city = models.CharField(max_length=15)
    postal_code = models.IntegerField(default=0)
    country = models.CharField(max_length=15, choices=COUNTRY_CHOICES, default='America')
    state = models.CharField(max_length=15)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    

class BidderUser(AbstractBaseUser, PermissionsMixin):
    COUNTRY_CHOICES = (('America', 'america'),
                       ('Germany', 'germany'),
                       ('Australia', 'australia'),
                       ('France', 'france'),)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(_('email address'),unique=True)
    email1 = models.EmailField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    company_name = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    telephone = models.IntegerField(default=0,blank=True)
    address1 = models.TextField(max_length=20)
    address2 =models.TextField(max_length=20, blank=True)
    city = models.CharField(max_length=15)
    postal_code = models.IntegerField(default=0)
    country = models.CharField(max_length=15, choices=COUNTRY_CHOICES, default='America')
    state = models.CharField(max_length=15)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name