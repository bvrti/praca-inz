from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth.decorators import login_required

from .forms import reportMalfunctionForm
# Create your views here.

def index(request):
    template = loader.get_template('app/index.html')
    if request.user_agent.is_mobile:
        return reportMalfunction(request)
    return HttpResponse(template.render({}, request))

@login_required(login_url='/login/')
def reportMalfunction(request):
    if request.POST:
        form = reportMalfunctionForm(request.POST)
        print(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save(using='postgres')
            return redirect('reportMalfunctionSuccess')
    template = loader.get_template('app/report-malfunction.html')
    return HttpResponse(template.render({ 'form' : reportMalfunctionForm }, request))

@login_required(login_url='/login/')
def reportMalfunctionSuccess(request):
    template = loader.get_template('app/report-malfunction-success.html')
    return HttpResponse(template.render({}, request))
# @login_required(login_url='/login/')
# def reportMalfunctionMobile(request):
#     template = loader.get_template('app/report-malfunction-mobile.html')
#     return HttpResponse(template.render({}, request))

