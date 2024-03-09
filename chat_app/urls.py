from django.urls import path
from . import views

urlpatterns = [
    path('acceuil', views.chatbot ,name ='chabot'),
   
   
]