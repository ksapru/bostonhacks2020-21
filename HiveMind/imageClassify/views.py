from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import FileClassify

def index(request):
    value = FileClassify.Files()
    output = "Hello, world. Imgae page." + value.f1()
    return HttpResponse(output)