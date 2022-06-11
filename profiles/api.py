from database.models import CustomUser, Session, VolunteerRequest
from rest_framework import viewsets, permissions, generics
from .serializers import VolunteerSerializer, OrganizationSessionsSerializer, VolunteerRequestSerializer, CustomUserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Get Volunteer API
class CustomUserAPI(generics.RetrieveAPIView):
    permissions_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user


@api_view(['GET'])
def getVolunteerRequests(request):
    if request.user.is_authenticated:
        requestV = VolunteerRequest.objects.filter(organization=request.user)
        request_serializer = VolunteerRequestSerializer(requestV, many=True)
        return Response(request_serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def updatePersonalData(request):
    if request.user.is_authenticated:
        user_serializer = CustomUserSerializer(request.user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Primero debe iniciar sesion"}, status=status.HTTP_400_BAD_REQUEST)
