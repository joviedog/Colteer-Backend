from rest_framework import serializers
from database.models import Session, CustomUser, VolunteerRequest, Turn

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

class SessionSerializer(serializers.ModelSerializer):

    volunteer = UserSerializer(many = True, read_only = True)

    class Meta:
        model = Session
        fields = '__all__'


class VolunteerRequestSerializer(serializers.ModelSerializer):

    volunteer = UserSerializer(many=True, read_only=True)

    class Meta:
        model = VolunteerRequest
        fields = '__all__'


class TurnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turn
        fields = '__all__'
