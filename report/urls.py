from django.urls import URLPattern, path, include
from report.api import *

urlpatterns = [
    path('api/statistics/number-of-volunteers', get_number_volunteers, name = "number_of_volunteers"),
    path('api/statistics/donations', donations_by_organization, name = "statistics_donations"),
    path('api/statistics/volunteers-by-month', volunteers_by_month, name = "statistics_volunteer_by_month"),


]