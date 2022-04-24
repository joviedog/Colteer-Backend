from rest_framework import serializers
from database.models import Volunteer, Organization, CustomUser
from django.contrib.auth import authenticate 
from django.contrib.auth.hashers import make_password, check_password

# CustomUserSerializer
# Volunteer Serializer
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        exclude = ['username', 'email', 'name']

# Volunteer Serializer
class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Volunteer
        exclude = ['last_login','is_superuser', 'first_name', 'last_name','is_staff','is_active', 'id','groups','user_permissions','password']

# Organization Serializer
class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model=Organization
        exclude = ['nit', 'type','last_login','is_superuser', 'first_name', 'last_name','is_staff','is_active', 'id','groups','user_permissions','password']



# Register Volunteer Serializer
class RegisterVolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Volunteer 
        fields =  ['birthday', 'phone','password', 'username']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        volunteer = Volunteer.objects.create(
            username=validated_data['username'],
            name=validated_data['name'],
            email=validated_data['email'],
            birthday=validated_data['birthday'],
            phone=validated_data['phone'],
            password=make_password(validated_data['password'])
        )
        return volunteer

# Register Organization Serializer
class RegisterOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Organization
        fields = ['name', 'email', 'nit', 'type', 'phone', 'password', 'username']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        organization = Organization.objects.create(
            username=validated_data['username'],
            name=validated_data['name'],
            email=validated_data['email'],
            nit=validated_data['nit'],
            type=validated_data['type'],
            phone=validated_data['phone'],
            password=make_password(validated_data['password'])
        )
        return organization

# Login Volunteer Serializer
class LoginVolunteerSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = Volunteer.objects.get(email=data['email'])
        check_pw = check_password(data['password'], user.password)
        if check_pw and user.is_active:
            return user 

        raise serializers.ValidationError("Credenciales incorrectas, verifique")

# Login Volunteer Serializer
class LoginOrganizationSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = Organization.objects.get(email=data['email'])
        check_pw = check_password(data['password'], user.password)
        if check_pw and user.is_active:
            print(user)
            return user 

        raise serializers.ValidationError("Credenciales incorrectas, verifique")

 