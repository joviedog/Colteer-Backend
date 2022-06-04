from rest_framework import serializers
from database.models import CustomUser
from django.contrib.auth import authenticate 
from django.contrib.auth.hashers import make_password, check_password



# CustomUserSerializer
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'document', 'phone', 'user_type']



# Volunteer Serializer
class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields = ['username', 'email', 'name', 'document', 'phone', 'birthday']

# Organization Serializer
class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model=CustomUser
        fields = ['username', 'email','name', 'document', 'phone', 'org_type']



# Register Volunteer Serializer
class RegisterVolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username', 'email', 'name', 'document', 'phone', 'birthday', 'password']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        volunteer = CustomUser.objects.create_user(
            username=validated_data['username'],
            document=validated_data['document'],
            name=validated_data['name'],
            phone=validated_data['phone'],
            email=validated_data['email'],
            birthday=validated_data['birthday'],
            user_type="Volunteer",
            password=validated_data['password']
        )
        return volunteer

# Register Organization Serializer
class RegisterOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name',
                  'document', 'phone', 'org_type', 'password']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        organization = CustomUser.objects.create_user(
            username=validated_data['username'],
            document=validated_data['document'],
            name=validated_data['name'],
            phone=validated_data['phone'],
            email=validated_data['email'],
            user_type="Organization",
            org_type=validated_data['org_type'],
            password=validated_data['password']
        )
        return organization


# Login Serializer for all classes
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = CustomUser.objects.get(email=data['email'])
        check_pw = check_password(data['password'], user.password)
        if check_pw and user.is_active:
            return user 

        raise serializers.ValidationError("Credenciales incorrectas, verifique")

