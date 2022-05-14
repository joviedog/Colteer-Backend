from django.urls import URLPattern, path, include
from donations.api import  donate, getDonations, getDonnors, myDonations
from search.api import *

urlpatterns = [
    path('api/donations/give',
         donate, name="api_donate"),
    path('api/donations/my-donations',
         myDonations, name="api_my_donations"),
    path('api/donations/donners',
         getDonations, name="api_get_donations"),
    path('api/donations/received',
         getDonnors, name="api_get_donnors"),
]
