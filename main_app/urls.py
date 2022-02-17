from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('cities/', views.CityList.as_view(), name="city_list"),
    path('cities/new', views.CityCreate.as_view(), name="city_create"),
    path('cities/<int:pk>/', views.CityDetail.as_view(), name ="city_detail"),
    path('cities/<int:pk>/update', views.CityUpdate.as_view(), name ="city_update"),
    path('cities/<int:pk>/delete', views.CityDelete.as_view(), name ="city_delete"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('cities/<int:pk>/posts/new/', views.PostCreate.as_view(), name="post_create"),
    path('cities/<int:pk>/post/update', views.PostUpdate.as_view(), name ="post_update"),
    path('cities/<int:pk>/post/delete', views.PostDelete.as_view(), name ="post_delete"),
    path('accounts/<int:pk>/profile', views.UserProfile.as_view(), name="user_profile"),
    path('accounts/<int:pk>/profile/update', views.ProfileUpdate.as_view(), name="profile_update"),
]