from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('cities/', views.CityList.as_view(), name="city_list")
]