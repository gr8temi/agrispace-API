from rest_framework.test import APITestCase
from rest_framework import status
# Create your tests here.
class Test(APITestCase):
    def test_travis(self):
        self.assertEqual(1+1,2)

class GetInformation(APITestCase):
    def test_get_information(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,status.HTTP_200_OK)