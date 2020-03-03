import json

from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from configuration.entity.recipe import Recipe
from configuration.entity.recipe_beverage import RecipeBeverage
from configuration.facade.recipe_beverage_facade import RecipeBeverageFacade


def get_index(request, _id=0):
    entities = []
    result = []
    id = 0

    try:
        id = int(_id)
    except (TypeError, ValueError):
        return HttpResponseBadRequest()

    if id <= 0:
        entities = RecipeBeverageFacade().find_all()
    elif id >= 1:
        entities = RecipeBeverageFacade().find_by_recipe(Recipe(id))

    for e in entities:
        result.append(e.__dict__)

    return JsonResponse(result, safe=False)


def _parse_entity(json):
    entity = RecipeBeverage()
    columns = ["id", "recipe_id", "beverage_id", "milliliters"]

    for column in columns:
        if column in json and hasattr(entity, column):
            setattr(entity, column, json[column])

    return entity


def put_index(request):
    entity_json = json.loads(request.body.decode("utf-8"))
    entity = _parse_entity(entity_json)
    result = RecipeBeverageFacade().update(entity)
    return JsonResponse(result.__dict__, safe=False)


def post_index(request):
    entity_json = json.loads(request.body.decode("utf-8"))
    entity = _parse_entity(entity_json)
    result = RecipeBeverageFacade().insert(entity)
    return JsonResponse(result.__dict__, safe=False)


def delete_index(request, _id):
    id = 0

    try:
        id = int(_id)
    except (TypeError, ValueError):
        return HttpResponseBadRequest()

    RecipeBeverageFacade().delete(id)
    return HttpResponse()


@csrf_exempt
def index(request, id=0):
    if request.method == "GET":
        return get_index(request, id)
    elif request.method == "PUT":
        return put_index(request)
    elif request.method == "POST":
        return post_index(request)
    elif request.method == "DELETE":
        return delete_index(request, id)
    else:
        return HttpResponseBadRequest()