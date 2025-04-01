from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    # card 에서 댓글을 쓰고 저장할 것이기 때문에 path 지정 X
    path('<int:post_id>/comment/create/', views.comment_create, name='comment_create'),
    path('<int:post_id>/like', views.like, name='like'),
    
]