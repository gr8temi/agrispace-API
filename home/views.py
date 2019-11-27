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
	"""
	This is the API view for getting all categories
	"""

	def get(self, request, *args, **kwargs):
		queryset = Category.objects.all()
		data = CategorySerializers(queryset, many=True).data
		return Response({"record":data},status=status.HTTP_200_OK)