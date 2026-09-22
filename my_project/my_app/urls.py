from django.urls import path
from my_app.views import *


urlpatterns = [
    path('',home_view,name='home')
]