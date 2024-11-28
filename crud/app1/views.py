from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import *

def signup(request):
    return render(request,"signup.html")

