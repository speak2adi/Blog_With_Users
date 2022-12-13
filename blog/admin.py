from django.contrib import admin
from .models import PostDb, CommentDb

# Register your models here.
admin.site.register(PostDb)
admin.site.register(CommentDb)