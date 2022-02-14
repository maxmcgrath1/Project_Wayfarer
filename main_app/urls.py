from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('cities/', views.CityList.as_view(), name="city_list"),
    path('cities/new', views.CityCreate.as_view(), name="city_create"),
    path('cities/<int:pk>/', views.CityDetail.as_view(), name ="city_detail"),
    path('cities/<int:pk>/update', views.CityUpdate.as_view(), name ="city_update"),
    path('cities/<int:pk>/delete', views.CityDelete.as_view(), name ="city_delete"),
    path('cities/<int:pk>/posts/new/', views.PostCreate.as_view(), name="song_create"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]