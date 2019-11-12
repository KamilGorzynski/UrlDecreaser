from django.urls import path
from .views import home_response, redirect_to_big_link, display_short_link


urlpatterns = [
    path('home/', home_response, name='home'),
    path('<str:shortcut>/', redirect_to_big_link),
    # path('new_url/', display_short_link, name='new_url'),
]
