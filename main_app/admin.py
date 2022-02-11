from django.contrib import admin
from .models import City, Post, Profile

# Register your models here.


admin.site.register(City)
admin.site.register(Post)
admin.site.register(Profile)