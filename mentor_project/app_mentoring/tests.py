from django.test import TestCase
from django.urls import reverse
from django_dynamic_fixture import G, F

from rest_framework.test import APIClient
from rest_framework import status

from .models import *
from .views import NodeAPIView, UsersByNodeListAPIView


class NodeAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        # mock objects
        self.node = G(
            PioNode, 
            name='PionerasDev',
            city='cali'
        )
        self.another_node = G(
            PioNode,
            name='PionerasDev',
            city='Bucaramanga'
        )

        self.fulana = G(
            User,
            username='Fulana',
            email='fula123@mail.com'
        )
        self.fulana_profile = G(
            UserProfile,
            user=self.fulana,
            pionode=self.node,
            role='Backend'
        )

        self.pepito = G(
            User,
            username='Pepito',
            email='pepito123@mail.com'
        )
        self.pepito_profile = G(
            UserProfile,
            user=self.pepito,
            pionode=self.node,
            role='Backend'
        )

    def test_can_get_node(self):
        url = reverse(
            NodeAPIView.name, kwargs={"pk": self.node.id}
        )
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_can_delete_node(self):
        pass

    def test_can_update_node(self):
        pass

    def test_get_users_by_node(self):
        pass