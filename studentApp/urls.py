from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('create/',create,name='create'),
    path('profile-details/<int:id>/',profileDetails,name='profileDetails'),
]