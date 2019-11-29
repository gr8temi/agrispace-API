from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import InfoSerializers, CategorySerializers
from .models import Information,Category
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json
from django.http import QueryDict,Http404


def home(request):
  return JsonResponse(dict(message='Welcome to the Phonebook API', ticket="12345"), status=200)

class Info(APIView):
	"""
	Returns information about the company
	"""
	def get(self, request, *args, **kwargs):
		queryset = Information.objects.all()
		data = InfoSerializers(queryset, many=True).data

		return Response({"record":data},status=status.HTTP_200_OK)

class CategoryView(APIView):
	serializer_class = CategorySerializers
	
	def get(self, request, *args, **kwargs):
		"""
		This method returns all job categories

		- Returns Response with all job categories
		- Returns Status of the API call = (200 -> OK), (400 -> Bad request)
		"""
		queryset = Category.objects.all()
		data = CategorySerializers(queryset, many=True).data
		if data:
			return Response({"record":data},status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def post(self, request):
		"""
		This methods creates a new job category instance

		args:
		request(dictionary)-the data attribute of the request should contain:
			- category_name(string)- the name of the job category
			- description(string)- the description of the category
			- image(string)- the image to represent the category
			
		- Returns Response with a record of the job instance created 
		- Returns Status of the API call = (201 -> created), (400 -> Bad request)
	"""
		serializer = CategorySerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"record":serializer.data}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)