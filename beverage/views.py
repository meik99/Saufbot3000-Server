import json
from pprint import pprint

from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from configuration.entity.beverage import Beverage
from configuration.facade.beverage_facade import BeverageFacade


def get_index(request):
    beverages = BeverageFacade().find_all()
    result = []

    for beverage in beverages:
        result.append(beverage.__dict__)

    return JsonResponse(result, safe=False)


def post_index(request):
    beverage_json = json.loads(request.body.decode("utf-8"))
    beverage = BeverageFacade().insert(Beverage(
        name=beverage_json["name"]
    ))
    return JsonResponse(beverage.__dict__, safe=False)


def update_request(request):
    beverage_json = json.loads(request.body.decode("utf-8"))
    beverage = BeverageFacade().update(Beverage(
        id=beverage_json["id"],
        name=beverage_json["name"]
    ))
    return JsonResponse(beverage.__dict__, safe=False)


def delete_request(request, id):
    _id = 0

    try:
        _id = int(id)
    except (ValueError, TypeError):
        return HttpResponseBadRequest()

    if _id <= 0:
        return HttpResponseBadRequest()

    BeverageFacade().delete(_id)
    return HttpResponse()


@csrf_exempt
def index(request, id=-1):
    if request.method == "GET":
        return get_index(request)
    elif request.method == "POST":
        return post_index(request)
    elif request.method == "PUT":
        return update_request(request)
    elif request.method == "DELETE":
        return delete_request(request, id)
    return HttpResponseBadRequest()