from django.contrib import messages
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import department, employee
from django.core import serializers
import json


# Create your views here.
def index(request):
    return render(request, "index.html")


def getdata(request):
    template_name = 'dropdown.html'
    deptcontext = department.objects.all()
    empcontext = employee.objects.all()
    if request.method == 'POST':
        messages.success(request,"Application Accepted")

    return render(request, template_name, {'department': deptcontext, 'employee': empcontext})

