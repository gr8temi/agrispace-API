from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import InfoSerializers
from .models import Information
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json
from django.http import QueryDict,Http404


def home(request):
  return JsonResponse(dict(message='Welcome to the Phonebook API', ticket="12345"), status=200)

class Info(APIView):
	def get(self, request, *args, **kwargs):
		queryset = Information.objects.all()
		data = InfoSerializers(queryset, many=True).data

		return Response({"record":data},status=status.HTTP_200_OK)
