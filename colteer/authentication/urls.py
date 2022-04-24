
from django.urls import path, include
from .api import RegisterVolunteerAPI, RegisterOrganizationAPI, LoginOrganizationAPI, LoginVolunteerAPI, VolunteerAPI, OrganizationAPI
from knox import views as knox_views 

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register_volunteer', RegisterVolunteerAPI.as_view()),
    path('api/auth/register_organization', RegisterOrganizationAPI.as_view()),
    path('api/auth/login_volunteer', LoginVolunteerAPI.as_view()),
    path('api/auth/login_organization', LoginOrganizationAPI.as_view()),
    path('api/auth/volunteer', VolunteerAPI.as_view()),
    path('api/auth/organization', OrganizationAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),

]