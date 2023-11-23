
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    # path('completeTask/', views.completeTask, name='completeTask'),
    # path('deleteTask/', views.deleteTask, name='deleteTask'),
    # path('updateTask/', views.updateTask, name='updateTask'),
]
