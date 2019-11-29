from rest_framework.test import APITestCase
from rest_framework import status
import tempfile
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
    Category endpoint test
    """
    data = {
            "category_name": "Farmers",
            "description": "Work for Farmers",
            "image": tempfile.NamedTemporaryFile(suffix=".jpg").name
            }
    def test_create_categories(self):
        """
        This test validates: 
            - User can create job category instance
            - Response status code evaluates to = (201 -> created),
            - Response data contains category_name key with value Farmers
        """
        response = self.client.post("/categories/",self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["record"]["category_name"],"Farmers")

    def test_get_categories(self):
        """
        This test validates:
            - User can get all job categories from this endpoint
            - Response status code evaluates to =(200-> OK)
            - length of record in response data evaluate to 1
            - Response data contains category_name key with value Farmers 
        
        """
        self.client.post("/categories/",self.data)
        response = self.client.get("/categories/")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data["record"]),1)
        self.assertEqual(response.data["record"][0]["category_name"],"Farmers")
    