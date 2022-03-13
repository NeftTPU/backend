from django.contrib import admin
from .models import Collection, Layer, Pool, Image

admin.site.register(Collection)
admin.site.register(Pool)
admin.site.register(Image)
admin.site.register(Layer)

