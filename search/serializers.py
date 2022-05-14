from rest_framework import serializers
from database.models import Session, CustomUser


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

# Organization Serializer
class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name', 'document', 'phone', 'org_type']
