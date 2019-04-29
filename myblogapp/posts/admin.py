from django.contrib import admin

# Register your models here.
from .models import Post # class名

admin.site.register(Post) # class名
