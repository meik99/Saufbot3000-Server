import json

from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from configuration.entity.recipe import Recipe
from configuration.facade.recipe_facade import RecipeFacade


def get_index(request):
    recipes = RecipeFacade().find_all()
    result = []

    for r in recipes:
        result.append(r.__dict__)

    return JsonResponse(result, safe=False)


def put_index(request):
    recipe_json = json.loads(request.body.decode("utf-8"))
    result = RecipeFacade().update(
        Recipe(
            id=recipe_json["id"],
            name=recipe_json["name"]))
    return JsonResponse(result.__dict__, safe=False)


def post_index(request):
    recipe_json = json.loads(request.body.decode("utf-8"))
    recipe = Recipe()

    if "name" in recipe_json:
        recipe.name = recipe_json["name"]

    result = RecipeFacade().insert(recipe)
    return JsonResponse(result.__dict__, safe=False)


def delete_index(request, id):
    try:
        RecipeFacade().delete(int(id))
    except (ValueError, TypeError):
        return HttpResponseBadRequest()

    return HttpResponse()


@csrf_exempt
def index(request, id=0):
    if request.method == "GET":
        return get_index(request)
    elif request.method == "PUT":
        return put_index(request)
    elif request.method == "POST":
        return post_index(request)
    elif request.method == "DELETE":
        return delete_index(request, id)
    else:
        return HttpResponseBadRequest()