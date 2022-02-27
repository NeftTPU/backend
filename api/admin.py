from django.contrib import admin
from .models import Collection, Pattern, Pull, Image

admin.site.register(Collection)
admin.site.register(Pattern)
admin.site.register(Pull)
admin.site.register(Image)

