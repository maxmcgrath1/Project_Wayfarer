from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('cities/', views.CityList.as_view(), name="city_list"),
    path('cities/new', views.CityCreate.as_view(), name="city_create"),
    path('cities/<int:pk>/', views.CityDetail.as_view(), name ="city_detail"),
    path('cities/<int:pk>/update', views.CityUpdate.as_view(), name ="city_update"),
]