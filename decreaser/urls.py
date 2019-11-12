from django.urls import path
from .views import home_response, redirect_to_big_link


urlpatterns = [
    path('home/', home_response, name='home'),
    path('<str:shortcut>/', redirect_to_big_link),
]
