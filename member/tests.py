# from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from .models import CareGiver, Elder, CareGiving

from rest_framework.test import APITestCase
from rest_framework import status
# from rest_framework.authtoken.models import Token


class MemberTesting(TestCase):

    def test_create_care_giver(self):
        user = User.objects.create_user(
                username="kaqfa", password="123", email="fahri@dinus.ac.id",
                first_name="fahri", last_name="firdausillah")
        CareGiver.objects.create(user=user, phone="0123456789")
        self.assertEqual(CareGiver.objects.count(), 1)
        cg = CareGiver.objects.get(pk=1)
        self.assertEqual(cg.user.first_name, "fahri")

    def test_create_elder(self):
        user = User.objects.create_user(
                username="kaqfa", password="123", email="fahri@dinus.ac.id",
                first_name="fahri", last_name="firdausillah")
        cg = CareGiver.objects.create(user=user, phone="0123456789")
        user2 = User.objects.create_user(
                username="ABC12", password="pwd", first_name="Ahmad",
                last_name="Tafrikhan")
        eld = Elder.objects.create(user=user2)
        CareGiving.objects.create(elder=eld, caregiver=cg)
        self.assertEqual(Elder.objects.count(), 1)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(eld.user.last_name, 'Tafrikhan')


class MemberService(APITestCase):

    def setUp(self):
        self.cguser = User.objects.create_user(
                username="kaqfa", password="123", email="fahri@dinus.ac.id",
                first_name="fahri", last_name="firdausillah")
        cg = CareGiver.objects.create(user=self.cguser, phone="0123456789")
        self.elduser = User.objects.create_user(
                username="ABC12", password="pwd", first_name="Ahmad",
                last_name="Tafrikhan")
        eld = Elder.objects.create(user=self.elduser)
        CareGiving.objects.create(elder=eld, caregiver=cg)
        # token = Token.objects.create(user=self.cguser)
        # token.save()

    def _require_login(self):
        self.client.login(username='kaqfa', password='123')

    def test_check_url_exist(self):
        resp = self.client.post('/api/members', {}, format="json")
        self.assertNotEqual(resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_caregiver_registrations(self):
        resp = self.client.post('/api/members/', {}, format="json")
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        data = {"username": "ingsun", "password": "firdaus123",
                "email": "ingsun@gmail.com",
                "fullname": "Fahri Firdausillah",
                "phone": "08989987517", "type": "c"}
        resp = self.client.post('/api/members/', data, format="json")
        # self.assertEqual(resp.content, data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CareGiver.objects.count(), 2)

    def test_empty_login(self):
        resp = self.client.post('/api/login/', {}, format="json")
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST,
                         resp.data)

    def test_caregive_login(self):
        resp = self.client.post('/api/login/',
                                {"username": "kaqfa", "password": "123"},
                                format="json")
        self.assertEqual(resp.status_code, status.HTTP_200_OK, resp.content)

    def test_elder_input(self):
        data = {"fullname": "Muhsiatun", "phone": "012345678910",
                "cared_by": ["1"], "type": "e"}

        # without login should be failed
        resp = self.client.post('/api/members/', data, format="json")
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        # after login it's okay
        self._require_login()
        resp = self.client.post('/api/members/', data, format="json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED,
                         resp.content)

    def test_elder_login(self):
        resp = self.client.post('/api/login/elder/', {}, format="json")
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST,
                         resp.content)

        resp = self.client.post('/api/login/elder/',
                                {'code': "ABC12"}, format="json")
        self.assertEqual(resp.status_code, status.HTTP_200_OK, resp.content)
