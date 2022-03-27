import io

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from api.models import Pool, Collection, Layer, Image
from PIL import Image as Img
from django.utils.crypto import get_random_string
from django.core.files.images import ImageFile
import time
import os


class Command(BaseCommand):
    help = u'Генерация пула'

    def add_arguments(self, parser):
        parser.add_argument('ID', type=int, help=u'ID')

    def handle(self, *args, **kwargs):
        id = kwargs['ID']

        pool = Pool.objects.get(pk=id)

        collections = Collection.objects.filter(pool=pool).all().order_by('height')

        n = len(collections)
        collections_sizes = []
        total = 1

        for collection in collections:
            collections_sizes.append(len(Layer.objects.filter(collection=collection).all()))

        for s in collections_sizes:
            total *= s
        dtotal = total

        generator_map = []
        for i in range(len(collections_sizes)):
            generator_map.append([])
            dtotal /= collections_sizes[i]
            f = 0
            k = 0
            for j in range(total):
                generator_map[i].append(k)
                f += 1
                if f == dtotal:
                    k += 1
                    if k == collections_sizes[i]:
                        k = 0
                    f = 0

        for i in range(total):
            result = Image()
            for j in range(len(collections_sizes)):
                layer = (Layer.objects.filter(collection=collections[j]).all())[generator_map[j][i]]
                layer_image = Image.objects.get(layer=layer)
                if j == 0:
                    image = Img.open(layer_image.file)
                else:
                    new_layer = Img.open(layer_image.file)
                    image.paste(new_layer, (0, 0), new_layer)

            output = io.BytesIO()
            image.save(output, format='PNG')
            output.seek(0)
            image_name = str(time.time()) + '_' + 'result.png'
            result.name = image_name
            result.file.save(image_name, output, save=False)
            result.save()
            pool.images.add(result)

        pool.is_generated = True
        pool.save()
