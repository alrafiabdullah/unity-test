from django.urls import path

from . import views

urlpatterns = [
    path('dummy', views.Index().as_view(), name='index'),
    path('subscribe', views.EmailSubscriptionView(
    ).as_view(), name='email_subscribe'),

    path('', views.subscribe_view, name='subscribe'),
]
