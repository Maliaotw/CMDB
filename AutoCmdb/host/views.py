from django.shortcuts import render, HttpResponse
from host import models


# Create your views here.
def index(requesrt):
    host_obj = models.Host.objects.all()

    data = {'data': host_obj}

    return render(requesrt, "host/index.html", data)
