from atexit import register
from django.contrib import admin
from .models import SlackDetail

admin.site.register(SlackDetail)
