import json

from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from configuration.entity.pump import Pump
from configuration.facade.pump_facade import PumpFacade


def get_index(request):
    pumps = PumpFacade().find_all()
    result = []

    for pump in pumps:
        result.append(pump.__dict__)

    return JsonResponse(result, safe=False)


def put_index(request):
    pump_request = json.loads(request.body.decode("utf-8"))
    result = PumpFacade().update(Pump(
        id=pump_request["id"],
        beverageId=pump_request["beverageId"]
    ))

    return JsonResponse(result.__dict__, safe=False)


@csrf_exempt
def index(request):
    if request.method == "GET":
        return get_index(request)
    elif request.method == "PUT":
        return put_index(request)
    else:
        return HttpResponseBadRequest()