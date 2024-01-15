from django.shortcuts import render
from . import serializers
from . import models



def index(request): 
    return render(request, "core/index.html",)


    