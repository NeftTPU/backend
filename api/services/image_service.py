from django.core.files import File
from ..models import Image
import time


class ImageService:
    def store(self, file: File):
        model = Image()
        file.name = str(time.time()) + '_' + file.name
        model.file = file
        model.save()

        return model
