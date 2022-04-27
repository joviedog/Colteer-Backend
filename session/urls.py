from django.urls import URLPattern, path, include
from session.api import *

urlpatterns = [
    path('api/sessions/', get_sessions, name = "api_get_sessions"),
    path('api/sessions/create-session', insert_session, name = "api_insert_session"),
    path('api/sessions/session/<int:id>', get_session_by_id, name = "api_get_detail_session"),
    path('api/sessions/session/<int:id>/update', update_session, name = "api_update_session"),
    path('api/sessions/session/<int:id>/delete', delete_session, name = "api_delete_session"),
]