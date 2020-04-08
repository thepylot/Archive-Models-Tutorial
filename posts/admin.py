from django.contrib import admin

from .models import Post, PostArchive

admin.site.register(Post)
admin.site.register(PostArchive)

