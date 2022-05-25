from rest_framework import serializers
from database.models import Session, CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

class SessionSerializer(serializers.ModelSerializer):

    volunteer = UserSerializer(many = True, read_only = True)

    class Meta:
        model = Session
        fields = '__all__'

