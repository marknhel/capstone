from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, you're in the management index!")

def blocked(request):

    return render(request, 'server_management/blocked.html')
