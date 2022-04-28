from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory
from database.models import CustomUser, Category
from session.api import *

class SessionsTesting(TestCase):
    def setUp(self):
        self.user = CustomUser(
            email='testing_login@dev.com',
            name='Testing',
            document='1234567',
            phone='3103345678',
            birthday='2001-10-10',
            user_type='Voluntario',
            username='testing_login'
        )
        self.user.set_password('admin123')
        self.user.save()
        self.category = Category(name = "Categoria de prueba")
        self.category.save()
        self.organization = CustomUser(
            email='testing_login2@dev.com',
            name='Testing2',
            document='12345678',
            phone='3103345678',
            birthday='2001-10-10',
            user_type='Organization',
            username='testing_login2'
        )
        self.organization.save()
        
        self.session = Session(
            id = 100,
            name = "Test",
            date = "2022-04-27T21:09:44Z",
            start_time = "21:09:46",
            end_time = "21:09:46",
            description = "Test",
            category = self.category,
            organization = self.organization,
        )
        self.session.volunteer.set([self.user])
        self.session.save()


    def test_get_sessions(self):
        
        factory = APIClient()
        request = factory.post('/api/auth/login', {
            "email": "testing_login@dev.com",
            "password": "admin123"
        })
        factory.credentials(HTTP_AUTHORIZATION='Token ' + request.data["token"])

        request = factory.get('/api/sessions/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_get_session(self):
        factory = APIClient()
        request = factory.post('/api/auth/login', {
            "email": "testing_login@dev.com",
            "password": "admin123"
        })
        factory.credentials(HTTP_AUTHORIZATION='Token ' + request.data["token"])

        request = factory.get('/api/sessions/session/2')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_insert_session(self):
        factory = APIClient()
        request = factory.post('/api/auth/login', {
            "email": "testing_login@dev.com",
            "password": "admin123"
        })
        factory.credentials(HTTP_AUTHORIZATION='Token ' + request.data["token"])

        request = factory.post('/api/sessions/create-session', {
            "id": 100,
            "name": "Test",
            "date": "2022-04-27T21:09:44Z",
            "start_time": "21:09:46",
            "end_time": "21:09:46",
            "description": "Test",
            "category": self.category.id,
            "organization": self.organization.id,
            "volunteer": [
                self.user.id
            ]
        })
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_update_session(self):
        factory = APIClient()
        request = factory.post('/api/auth/login', {
            "email": "testing_login@dev.com",
            "password": "admin123"
        })
        factory.credentials(HTTP_AUTHORIZATION='Token ' + request.data["token"])
        request = factory.put('/api/sessions/session/2/update', {
            "name": "Test Actualizado",
            "date": "2022-04-27T21:09:44Z",
            "start_time": "21:09:46",
            "end_time": "21:09:46",
            "description": "Test Actualizado",
            "category": self.category.id,
            "organization": self.organization.id,
            "volunteer": [
                self.user.id
            ]
        })
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_delete_session(self):
        factory = APIClient()
        request = factory.post('/api/auth/login', {
            "email": "testing_login@dev.com",
            "password": "admin123"
        })
        factory.credentials(HTTP_AUTHORIZATION='Token ' + request.data["token"])
        request = factory.delete('/api/sessions/session/'+str(self.session.id)+'/delete')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

        


