from django.http import HttpResponse
from django.shortcuts import render
import django.http

# Create your views here.
def index(request, id=0):

    return HttpResponse(status=201)