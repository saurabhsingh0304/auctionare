from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import VendorUser


class VendorCreationForm(UserCreationForm):
    class Meta:
        model = VendorUser
        fields = ('first_name', 'last_name', 'email', 'email1', 'password1', 'password2',
                  'company_name', 'mobile', 'telephone', 'address1', 'address2', 'city', 'postal_code', 'country', 'state')


class BidderCreationForm(UserCreationForm):
    class Meta:
        model = VendorUser
        fields = ('first_name', 'last_name', 'email', 'email1', 'password1', 'password2',
                  'company_name', 'mobile', 'telephone', 'address1', 'address2', 'city', 'postal_code', 'country', 'state')
