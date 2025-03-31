from django.db import models
from django_resized import ResizedImageField
from django.conf import settings

# Create your models here.

class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='image')
    # 이미지 필드를 위해서는 pillow가 필요
    image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to='image/%y/%m',
    )