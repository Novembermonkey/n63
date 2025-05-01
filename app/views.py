from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

def title(request):
    data ="Hello world"
    return HttpResponse(data)
