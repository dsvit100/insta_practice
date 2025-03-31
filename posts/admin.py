from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.register(Post)
# 어드민 페이지에서 Post 탭을 관리하겠다
