from rest_framework import generics, permissions
from rest_framework.response import Response 
from knox.models import AuthToken
from .serializers import VolunteerSerializer, OrganizationSerializer, RegisterVolunteerSerializer, RegisterOrganizationSerializer, LoginSerializer, CustomUserSerializer

# Register Volunteer API
class RegisterVolunteerAPI(generics.GenericAPIView):
    serializer_class = RegisterVolunteerSerializer


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        volunteer = serializer.save()
        return Response({
            "user": VolunteerSerializer(volunteer, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(volunteer)[1]
        }) 

        
# Register Organization API
class RegisterOrganizationAPI(generics.GenericAPIView):
    serializer_class = RegisterOrganizationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        organization = serializer.save()
        return Response({
            "user": OrganizationSerializer(organization, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(organization)[1]
        })



# Login Volunteer API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": CustomUserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


# Get Volunteer API
class VolunteerAPI(generics.RetrieveAPIView):
    permissions_classes = [
        permissions.IsAuthenticated,
        ]
    serializer_class = VolunteerSerializer

    def get_object(self):
        return self.request.user


# Get Organization API
class OrganizationAPI(generics.RetrieveAPIView):
    permissions_classes = [
        permissions.IsAuthenticated,
        ]
    serializer_class = OrganizationSerializer

    def get_object(self):
        return self.request.user



