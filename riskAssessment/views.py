from django.http import JsonResponse
from django.shortcuts import render
from .src import riskEngine, riskDict
import json

def index(request):
    if len(request.POST) == 0:
        # Load landing page with a form to be filled.
        return render(request, 'index.html', {})
    else:
        # Receive data from the form and provide a response.
        print(request.POST['age'])
        inputProfile = riskDict.treatInput(request.POST)
        context = riskEngine.computeRisk(inputProfile)
        return render(request, 'result.html', context)

def result(request):
    # Method is used only when called by an external source using GET.
    try:
        context = riskEngine.computeRisk(json.loads(request.body))
        return JsonResponse(context)
    except:
        return JsonResponse({})