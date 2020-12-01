from rest_framework import serializers
from .models import VendorUser, BidderUser

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorUser
        fields = ('first_name', 'last_name', 'email', 'company_name', 'mobile', 'telephone', 
                'address1', 'address2', 'city', 'postal_code', 'country', 'state')


class BidderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BidderUser
        fields = ('first_name', 'last_name', 'email', 'company_name', 'mobile', 'telephone', 
                'address1', 'address2', 'city', 'postal_code', 'country', 'state')