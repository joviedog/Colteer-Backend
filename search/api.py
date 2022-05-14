from unicodedata import category
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from database.models import Session, CustomUser, Category
from search.serializers import SessionSerializer, OrganizationSerializer


@api_view(['GET'])
def sessionCategory(request):
    if request.user.is_authenticated:
        cat_id = Category.objects.filter(name=request.data['category'])[0].id
        if cat_id:
            sessionsByCategory = Session.objects.filter(id=cat_id)
            sessionsSerializer = SessionSerializer(sessionsByCategory, many=True)
            return Response(sessionsSerializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Categoria de busqueda invalida"}, status=status.HTTP_404_NOT_FOUND)
    return Response({"message": "Primero debe iniciar sesion"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def sessionDate(request):
    if request.user.is_authenticated:
        sessionsByCategory = Session.objects.filter(
            date=request.data['date'])
        sessionsSerializer = SessionSerializer(sessionsByCategory, many=True)
        return Response(sessionsSerializer.data, status=status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def organizationType(request):
    if request.user.is_authenticated:
        organizationsByType = CustomUser.objects.filter(user_type="Organization",
            org_type=request.data['org_type'])
        organizationsSerializer = OrganizationSerializer(organizationsByType, many=True)
        return Response(organizationsSerializer.data, status=status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def allOrganizations(request):
    if request.user.is_authenticated:
        organizations = CustomUser.objects.filter(user_type="Organization")
        orgSerializer = OrganizationSerializer(organizations, many=True)
        return Response(orgSerializer.data, status=status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status=status.HTTP_400_BAD_REQUEST)
