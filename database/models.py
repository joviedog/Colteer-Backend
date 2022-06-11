from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.deletion import CASCADE
from django.utils import timezone



# Create your models here.
class CustomUser(AbstractUser):
    class Meta:
        verbose_name = 'User'
    username = models.CharField(max_length=40, unique=True, default='')
    document = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=10, default='12345678')
    created_at = models.DateField(auto_now_add=True)
    # Type Identification for all users
    user_type = models.CharField(max_length=100)
    # Fields for volunteer
    birthday = models.DateField(default=timezone.now, null=True)
    # Fields for organizations
    org_type = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.name)
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Session(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
   
    SESSION_STATUS = [
        (0, "En espera"),
        (1, "Aprobado"),
        (2, "Rechazado"),
    ]
    status = models.IntegerField(choices = SESSION_STATUS, default = 0)
    
    # Foreign Keys and Relationships
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="Organizador")
    volunteer = models.ManyToManyField(CustomUser, related_name="Voluntario")

class VolunteerRequest(models.Model):
    SESSION_STATUS = [
        (0, "En espera"),
        (1, "Aprobado"),
        (2, "Rechazado"),
    ]
    status = models.IntegerField(choices=SESSION_STATUS, default=0)
    # Foreign keys and Relationships
    session = models.ForeignKey(
        Session, on_delete=models.CASCADE, related_name="SesionSolicitada")
    organization = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="OrganizacionOferente", default=None)
    volunteer = models.ManyToManyField(CustomUser, related_name="Solicitante")


class Turn(models.Model):
    available = models.IntegerField()
    full = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    # Foreign Keys and Relationships
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

class Donation(models.Model):
    value = models.FloatField()
    # Foreign Keys and Relationships
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="Donador")
    organization = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="Organizacion")
 
