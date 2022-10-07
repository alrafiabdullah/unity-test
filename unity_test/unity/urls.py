from django.urls import path

from . import views

urlpatterns = [
    path('dummy', views.Index().as_view(), name='index'),
]
