from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.deletion import CASCADE
from django.utils import timezone



# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=40, unique=True, default='')
    name = models.CharField(max_length=150)
    pass


class Volunteer(CustomUser):
    class Meta:
        verbose_name = 'Volunteer'
    birthday = models.DateField(default=timezone.now)
    phone=models.CharField(max_length=10, default='12345678')
    def __str__(self):
        return str(self.name)


class Organization(CustomUser):  
    class Meta:
        verbose_name = 'Organization'
    nit = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=100)
    phone=models.CharField(max_length=10, default='12345678')
    created_at = models.DateField(auto_now_add=True)

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
    # Foreign Keys and Relationships
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    volunteer = models.ManyToManyField(Volunteer)



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
    user = models.ForeignKey(Volunteer, on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
 