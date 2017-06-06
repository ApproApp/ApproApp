from django.shortcuts import render, HttpResponse
# Create your views here.

        

def home(request):
    render(request, 'index.html')