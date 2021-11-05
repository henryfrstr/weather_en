from django.urls import path
from .views import home, delte_city
urlpatterns = [
    path('', home, name='home'),
    path('delete/<id>', delte_city, name='delete'),
]
