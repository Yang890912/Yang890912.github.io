from week10project import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('ccu408410043', views.ccu408410043_function)
]
