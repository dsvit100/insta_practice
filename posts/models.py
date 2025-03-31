from django.db import models

# Create your models here.

class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='image')
    # 이미지 필드를 위해서는 pillow가 필요