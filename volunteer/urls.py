from django.urls import URLPattern, path, include
from volunteer.api import *

urlpatterns = [
    path('api/volunteer/register-volunteer', api_register_volunteer, name = "api_register_volunteer"),
    
]