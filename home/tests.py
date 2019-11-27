from rest_framework.test import APITestCase
from rest_framework import status
# Create your tests here.
class Test(APITestCase):
    """
    Runs basic test
    """
    def test_travis(self):
        self.assertEqual(1+1,2)

class InformationTest(APITestCase):
    """
    Runs test on Information fetching endpoint
    """
    def test_get_information(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,status.HTTP_200_OK)

class CategoryTest(APITestCase):
    """
    This test validates get method on Categories API
    """
    def test_get_categories(self):
        response = self.client.get("/categories/")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    