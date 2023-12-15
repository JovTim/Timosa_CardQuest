from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('trainer_list', TrainerList.as_view(), name="trainer-list"),
    path('trainer_list/add', TrainerCreateView.as_view(), name='trainer-add')
]
