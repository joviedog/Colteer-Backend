from database.models import CustomUser, Category, Session, Turn, Donation, VolunteerRequest
from rest_framework import serializers


class VolunteerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'email']


class OrganizationSessionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ['name', 'category', 'date', 'description']


class VolunteerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerRequest
        fields = ['session','organization','status']

# CustomUserSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'



