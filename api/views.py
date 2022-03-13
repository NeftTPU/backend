import json

from django.http import HttpResponse
from rest_framework import generics, mixins
from .serializers import *
from .services import ImageService, CollectionService, LayerService, PoolService


def json_response(data):
    return HttpResponse(json.dumps(data), content_type="application/json")


def store_image(request):
    image_file = request.FILES['image']
    image = ImageService().store(image_file)

    return json_response(ImageSerializer(image).data)


class CollectionAPIView(generics.GenericAPIView):
    def get(self, request):
        collections = CollectionService().getAllForUser(request.user)

        return json_response(CollectionWithLayerWithImageSerializer(collections, many=True).data)

    def post(self, request):
        collection = CollectionService().store(request.POST, request.user)

        return json_response(CollectionSerializer(collection).data)

    def delete(self, request, id):
        CollectionService().delete(id)
        return HttpResponse()

    def put(self, request, id):
        collection = CollectionService().update(id, request.POST, request.user)

        return json_response(CollectionSerializer(collection).data)


class LayerAPIView(generics.GenericAPIView):
    def post(self, request):
        layer = LayerService().store(request.POST)

        return json_response(LayerSerializer(layer).data)

    def delete(self, request, id):
        LayerService().delete(id)

        return HttpResponse()

    def put(self, request, id):
        layer = LayerService().update(id, request.POST)

        return json_response(LayerSerializer(layer).data)


class PoolListAPIView(generics.GenericAPIView):
    def get(self, request):
        pools = PoolService().getListForUser(request.user)

        return json_response(PoolSerializer(pools, many=True).data)

    def post(self, request):
        pool = PoolService().store(request.POST, request.user)

        return json_response(PoolSerializer(pool).data)


class PoolAPIView(generics.GenericAPIView):
    def get(self, request, id):
        pool = PoolService().getById(id)

        return json_response(PoolWithImagesSerializer(pool).data)
