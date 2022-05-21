from rest_framework import serializers
from database.models import Session, CustomUser, Category
from donations.serializers import CustomUserSerializer



class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name', 'document', 'phone', 'org_type']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()
    category = CategorySerializer()

    class Meta:
        model = Session
        fields = ['name', 'date', 'start_time', 'end_time',
                  'description', 'category', 'organization']
