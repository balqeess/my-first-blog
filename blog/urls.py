Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
