from rest_framework import serializers
from database.models import Session, CustomUser

class SessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    session = SessionSerializer(many = True, read_only = True)

    class Meta:
        model = CustomUser
        fields = "__all__"