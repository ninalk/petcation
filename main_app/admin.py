from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Owner, Sitter, Pet, Post, Photo, SitterPhoto


admin.site.register(Owner)
admin.site.register(Sitter)
admin.site.register(Pet)
admin.site.register(Post)
admin.site.register(Photo)
admin.site.register(SitterPhoto)