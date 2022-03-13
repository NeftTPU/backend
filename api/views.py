import json

from django.http import HttpResponse
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import authentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Collection, Pool, Image
from .serializers import CollectionSerializer, PoolSerializer, ImageSerializer

from .services import ImageService
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def store_image(request):
    image_file = request.FILES['image']
    image = ImageService().store(image_file)

    return HttpResponse(json.dumps(ImageSerializer(image).data), content_type="application/json")


def get_image(id: int):
    image = ImageService().getById(id)

    return Response(ImageSerializer(image).data)
