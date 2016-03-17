from django.contrib.auth.models import User
# from tracker.models import Tracker

from rest_framework.test import APITestCase
from rest_framework import status


class TrackerServiceTests(APITestCase):

    fixtures = ['auth.json', 'member.json', 'tracker.json']

    def _cg_login(self):
        return self.client.login(username='kaqfa', password='123')

    def _eld_login(self):
        return self.client.login(username='ABC12', password='pwd')

    def test_list_conditions(self):
        resp = self.client.get('/api/trackers/', format="json")
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

        self._cg_login()
        resp = self.client.get('/api/trackers/', format="json")
        # print(resp.content)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_post_conditions(self):
        user = User.objects.get(username="ABC12")
        data = {"condition": "sll", "elder": user.elder.id}

        resp = self.client.post('/api/trackers/', data, format="json")
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

        self._eld_login()
        resp = self.client.post('/api/trackers/', data, format="json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED,
                         resp.content)
