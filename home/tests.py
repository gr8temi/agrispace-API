from rest_framework.test import APITestCase
# Create your tests here.
class Test(APITestCase):
    def test_travis(self):
        self.assertEqual(1+1,2)