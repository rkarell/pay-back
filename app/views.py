from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json

@ensure_csrf_cookie
def index(request):
    return render(request, 'index.html')

def solve(request):
    jsonData = json.loads(request.body)
    data = {
        'debts':jsonData["transactions"] + "2"
    }
    print(jsonData)
    return JsonResponse(data)