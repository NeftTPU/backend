from rest_framework import serializers
from .models import Collection, Layer, Pool, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class LayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layer
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class CollectionWithLayerWithImageSerializer(CollectionSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'date_created', 'height', 'layer_set']
        depth = 2


class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pool
        fields = '__all__'


class PoolWithImagesSerializer(PoolSerializer):
    class Meta:
        model = Pool
        fields = ['id', 'title', 'date_created', 'images']
        depth = 1
