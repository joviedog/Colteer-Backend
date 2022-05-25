from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from database.models import CustomUser
from volunteer.serializers import UserSerializer

@api_view(['GET'])
def api_register_volunteer(request):
    user = CustomUser.objects.all()
    user_serializer = UserSerializer(user, many = True)
    return Response(user_serializer.data, status = status.HTTP_200_OK)