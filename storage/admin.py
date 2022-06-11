from django.contrib import admin
from .models import *

admin.site.register(Image)
admin.site.register(Audio)
admin.site.register(Video)
admin.site.register(Document)