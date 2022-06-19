from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models.functions import ExtractMonth, ExtractYear
from django.db.models import Sum, Count
from database.models import CustomUser, Donation, Session


@api_view(["GET"])
def get_number_volunteers(request):
    result = CustomUser.objects.filter(user_type = "Volunteer").count()
    return Response({"number": result}, status = status.HTTP_200_OK)

@api_view(["GET"])
def donations_by_organization(request):
    # result = Donation.objects.values("organization").order_by("organization").annotate(total = Sum('value'))
    donations = Donation.objects.all()
    dictDonations = {}
    for donation in donations:
        if dictDonations.get(donation.organization.username, None):
            dictDonation = dictDonations[donation.organization.username]
            dictDonation["value"] += donation.value
            dictDonation["quantity"] += 1
            dictDonation["average"] = dictDonation['value'] / dictDonation['quantity']
            dictDonations[donation.organization.username] = dictDonation
        else:
            dictDonation = {}
            dictDonation['value'] = donation.value
            dictDonation["quantity"] = 1
            dictDonation["average"] = donation.value
            dictDonations[donation.organization.username] = dictDonation
    return Response(dictDonations, status = status.HTTP_200_OK)

@api_view(["GET"])
def volunteers_by_month(request):
    h = Session.objects.annotate(month=ExtractMonth('date'),
                                year=ExtractYear('date'),).order_by().values('month', 'year').annotate(total=Count('volunteer')).values('month', 'year', 'total')
    result = {"data": h}
    return Response(result, status = status.HTTP_200_OK)
    
    


