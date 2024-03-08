from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contact',views.contact),
    path('add',views.addStudent),
    path('insert',views.insertStudent),
    path('delete/<id>',views.delete),
    path('edit/<id>',views.edit),
    path('update/<id>',views.update),
    
]
