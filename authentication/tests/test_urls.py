# Django
from django.test import TestCase
# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status
from database.models import CustomUser

class AuthTesting(TestCase):
    def setUp(self):
        user = CustomUser(
            email='testing_login@dev.com',
            name='Testing',
            document='1234567',
            phone='3103345678',
            birthday='2001-10-10',
            user_type='Voluntario',
            username='testing_login'
        )
        user.set_password('admin123')
        user.save()

    def test_user_registration(self):
        factory = APIClient()

        request = factory.post('/api/auth/register_volunteer', {
            "username": "jmvelez",
            "name": "Jota Mario Velez",
            "email": "jmvelez@unal.edu.co",
            "document": "51445678",
            "birthday": "2001-10-07",
            "phone": "3103154567",
            "password": "ingesoft"
        })
        self.assertEqual(request.status_code, status.HTTP_200_OK)


    def test_user_login(self):
        factory = APIClient()

        request = factory.post('/api/auth/login', {
            "email": "testing_login@dev.com",
            "password": "admin123"
        })
        self.assertEqual(request.status_code, status.HTTP_200_OK)
