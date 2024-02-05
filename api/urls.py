from django.urls import path
from api import views


urlpatterns = [
    path('add_shorten/', views.shorten_url, name='shorten_url'),
    path('<str:short_url>/', views.access_url, name='access_url'),
]
