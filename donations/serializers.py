from rest_framework import serializers
from database.models import Donation, CustomUser

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'document', 'phone']

class CustomDonationSerializer(serializers.ModelSerializer):
    organization = CustomUserSerializer()

    class Meta:
        model = Donation
        fields = ('value', 'organization')


class CustomDonationSerializerOrg(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Donation
        fields = ('value', 'user')

    


