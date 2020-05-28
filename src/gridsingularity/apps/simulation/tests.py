from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from gridsingularity.apps.simulation.models import SimulationResult

class CreateSimulationTest(APITestCase):
    """
        Test crate silulation
    """

    def test_create_silulation(self):
        """
            Test if we get 200 response on post
        """
        url = reverse('create-simulation')
        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SimulationResult.objects.count(), 1)


class GetSimulationTest(APITestCase):
    """ 
        Test get Simulation
    """
    def setUp(self):
        SimulationResult.objects.create(active=0.50, reactive=0.2)
    
    def test_get_silulation(self):
        """
            Test object get by id successfully
        """
        response = self.client.get('/api/v1/simulations/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['active'], '0.50')
        self.assertEqual(response.data['reactive'], '0.20')

    def test_get_silulation_404(self):
        response = self.client.get('/api/v1/simulations/2/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class GetSimulationActiveTest(APITestCase):
    """ 
        Test get Simulation
    """
    def setUp(self):
        SimulationResult.objects.create(active=0.50, reactive=0.2)
    
    def test_get_silulation(self):
        """
            Test object get by id successfully
        """
        response = self.client.get('/api/v1/simulations/1/active/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['active'], '0.50')

    def test_get_silulation_404(self):
        response = self.client.get('/api/v1/simulations/2/active/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class GetSimulationReActiveTest(APITestCase):
    """ 
        Test get Simulation
    """
    def setUp(self):
        SimulationResult.objects.create(active=0.50, reactive=0.2)
    
    def test_get_silulation(self):
        """
            Test object get by id successfully
        """
        response = self.client.get('/api/v1/simulations/1/reactive/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['reactive'], '0.20')

    def test_get_silulation_404(self):
        response = self.client.get('/api/v1/simulations/2/reactive/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

