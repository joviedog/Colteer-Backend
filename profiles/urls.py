from django.urls import path, include
from knox import views as knox_views

from profiles.api import getVolunteerRequests, updatePersonalData, CustomUserAPI

urlpatterns = [
    path('api/profile/', getVolunteerRequests, name="volunteer_sessions"),
    path('api/profile/update_data', updatePersonalData, name="api_updateData"),
    path('api/profile/user_data', CustomUserAPI.as_view(), name='user_data'),
]
