from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.db import connection

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
            instance.save(using='default')
            return redirect('reportMalfunctionSuccess')
    template = loader.get_template('app/report-malfunction.html')
    return HttpResponse(template.render({ 'form' : reportMalfunctionForm }, request))

@login_required(login_url='/login/')
def reportMalfunctionSuccess(request):
    template = loader.get_template('app/report-malfunction-success.html')
    return HttpResponse(template.render({}, request))

@login_required(login_url='/login/')
def reportsopenedmalfunctions(request):
    template = loader.get_template('app/reports-opened-malfunctions.html')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM app_malfunction WHERE status != 'Closed'")
        malfunctions = cursor.fetchall()
    finally:
        cursor.close()
    return HttpResponse(template.render({ 'malfunctions' : malfunctions }, request))

@login_required(login_url='/login/')
def viewMalfunction(request, id):
    template = loader.get_template('app/viewMalfunction.html')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM app_malfunction WHERE id = %s;", [id])
        malfunction = cursor.fetchall()
    finally:
        cursor.close()
    return HttpResponse(template.render({'malfunction' : malfunction }, request))