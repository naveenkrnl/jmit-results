from django.urls import path
from .views import home

app_name='result'

urlpatterns = [
    path('', home,name='home'),
]
