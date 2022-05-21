from rest_framework import serializers
from database.models import Session, CustomUser
from donations.serializers import CustomUserSerializer


class SessionSerializer(serializers.ModelSerializer):
    volunteer = CustomUserSerializer
    class Meta:
        model = Session
        fields = ['name', 'date', 'start_time', 'end_time', 'description', 'category', 'organization']


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name', 'document', 'phone', 'org_type']
