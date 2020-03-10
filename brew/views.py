from django.http import HttpResponse
from django.shortcuts import render
import django.http

# Create your views here.
from configuration.facade.brew_facade import BrewFacade


def index(request, id=0):
    _id = int(id)
    BrewFacade().brew(_id)
    return HttpResponse(status=201)