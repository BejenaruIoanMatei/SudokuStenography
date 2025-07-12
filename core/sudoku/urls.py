from django.urls import path
from . import views

urlpatterns = [
    path('', views.encode_view, name='encode'),
]
