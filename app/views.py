from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render({}, request))

# def login(request):
#     template = loader.get_template('app/login.html')
#     return HttpResponse(template.render({}, request))