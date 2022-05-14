from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from database.models import Donation, Session, CustomUser, Category, CustomUser
from donations.serializers import DonationSerializer, CustomUserSerializer, CustomDonationSerializer, CustomDonationSerializerOrg


@api_view(['POST'])
def donate(request):
    if request.user.is_authenticated:
        curr_user = request.user.id
        org = CustomUser.objects.filter(user_type="Organization", name=request.data["organization"])[0].id
        value = request.data["value"]

        donationSerializer = DonationSerializer(data={"value":value, "user":curr_user, "organization":org})
        if donationSerializer.is_valid():
            donationSerializer.save()
            return Response(donationSerializer.data, status=status.HTTP_201_CREATED)
        return Response(donationSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Primero debe iniciar sesion"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def myDonations(request):
    if request.user.is_authenticated and request.user.user_type == 'Volunteer':
        donations = Donation.objects.filter(user=request.user)
        donationSerializer = CustomDonationSerializer(donations, many=True)
        return Response(donationSerializer.data, status=status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getDonations(request):
    if request.user.is_authenticated:
        donnors = Donation.objects.filter(
            organization=request.user).values("user")
        userSerializer = CustomDonationSerializer(donnors, many=True)
        return Response(userSerializer.data, status=status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getDonnors(request):
    if request.user.is_authenticated and request.user.user_type == 'Organization':
        donations = Donation.objects.filter(organization=request.user)
        donationSerializer = CustomDonationSerializerOrg(donations, many=True)
        return Response(donationSerializer.data, status=status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status=status.HTTP_400_BAD_REQUEST)


