from django.urls import path
from helloworld.views import hello_world

app_name = 'helloworld'

urlpatterns = [
    path('', hello_world, name='hello_world'),
]