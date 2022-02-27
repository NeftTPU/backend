from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import authentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Collection, Pattern, Pull, Image
from .serializers import CollectionSerializer, PatternSerializer, PullSerializer, ImageSerializer
