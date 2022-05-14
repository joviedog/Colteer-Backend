from django.urls import URLPattern, path, include
from search.api import *

urlpatterns = [
    path('api/search/sessions/by_category', sessionCategory, name="api_sessions_by_category"),
    path('api/search/sessions/by_date',
         sessionDate, name="api_sessions_by_date"),
    path('api/search/organization/by_category',
         organizationType, name="api_organization_by_category"),
    path('api/search/organization/all',
         allOrganizations, name="api_all_organizations"),
]
