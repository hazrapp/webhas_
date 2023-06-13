from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from  django.core.files.storage import FileSystemStorage
from django.conf import settings
from . models import *

def first(request):
    return render (request,'index.html')
def index(request):
    return render(request,'index.html')