
from django.urls import path


from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.show_blogs , name = 'show_blogs'),
    path('<int:blog_id>', views.detail , name = 'detail'),
]
