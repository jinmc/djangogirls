from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Job_Heykorean

admin.site.register(Post)
admin.site.register(Job_Heykorean)