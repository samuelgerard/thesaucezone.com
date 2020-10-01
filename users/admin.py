from django.contrib import admin
from .models import Profile

#set up so that admins can edit profiles and such
admin.site.register(Profile)
# Register your models here.
