from django.contrib import admin
from .models import (
    Comment,
    Post,
    Post_Owner
)
# Register your models here.
admin.site.register(Post)
admin.site.register(Post_Owner)
admin.site.register(Comment)