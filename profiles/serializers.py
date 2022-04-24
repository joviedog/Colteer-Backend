from database.models import Volunteer, Organization, Category, Session, Turn, Donation
from rest_framework import serializers


class VolunteerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Volunteer
        fields = ['name', 'email']


class OrganizationSessionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ['name', 'category', 'date', 'description']






