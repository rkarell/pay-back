from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from app.transactions import Transactions
from app.debts import Debts

@ensure_csrf_cookie
def index(request):
    return render(request, 'app/index.html')

def solve(request):
    jsonData = json.loads(request.body)
    transactions = Transactions()
    error = transactions.load(jsonData["transactions"])
    if error is None:
        debts = Debts()
        debts.addTransactions(transactions)
        debts.optimizeAlgorithm1()
        debts.optimizeAlgorithm2()
        result = str(debts)
    else:
        result = error

    data = {
            'debts':result
        }
    return JsonResponse(data)