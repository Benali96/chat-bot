from django.shortcuts import render
from .models import ChatBot
from django.http import HttpResponse



# Create your views here.def Menu (request):
def chatbot (request):
    return render(request ,{'ChatBot':ChatBot.objects.all()})
