from database.models import Volunteer, Organization, Session
from rest_framework import viewsets, permissions
from .serializers import VolunteerSerializer, OrganizationSessionsSerializer

# Volunteer Viewset
class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VolunteerSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = OrganizationSessionsSerializer

    def get_queryset(self):
        return Session.objects.all()

