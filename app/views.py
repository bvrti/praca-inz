from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    template = loader.get_template('app/index.html')
    if request.user_agent.is_mobile:
        return reportMalfunction(request)
    return HttpResponse(template.render({}, request))

@login_required(login_url='/login/')
def reportMalfunction(request):
    template = loader.get_template('app/report-malfunction.html')
    return HttpResponse(template.render({}, request))

# @login_required(login_url='/login/')
# def reportMalfunctionMobile(request):
#     template = loader.get_template('app/report-malfunction-mobile.html')
#     return HttpResponse(template.render({}, request))

