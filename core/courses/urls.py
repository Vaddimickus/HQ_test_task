from django.urls import path
from . import views


urlpatterns = [
    path('api1', views.index_api1, name="api1"),
    path('api2', views.index_api2, name="api2"),
    path('api3', views.index_api3, name="api3"),
]
