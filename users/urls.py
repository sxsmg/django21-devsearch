from django.urls import path 
from .views import profiles, userProfile, loginPage

urlpatterns = [

    path('login/', loginPage,name="login"),


    path('', profiles, name="profiles"),
    path('profile/<str:pk>/', userProfile, name="user-profile"),
    ]
   