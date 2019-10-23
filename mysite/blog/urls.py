from django.contrib import admin
from django.urls import path ,include
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('<int:number>/', views.detail,name="detail"),
    path('archive/', views.archive,name="archive"),
    path('contact/', views.contact,name="contact"),
    path('about/', views.about,name="about"),
]