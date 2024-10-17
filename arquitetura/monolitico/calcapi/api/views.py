from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET

# Create your views here.

@require_GET
def calc(request):
    res = {}
    res['resultado'] = "calc está funcionando! Versão 1.0"
    return JsonResponse(res)

@require_GET
def soma(request):
    op1 = request.GET.get("op1", "")
    if op1:
        print(f"{op1}")
    else:
        res = {}
        res['resultado'] = "op1 não informado"
        return JsonResponse(res)
    
    op2 = request.GET.get("op2", "")
    if op2:
        print(f"{op2}")
    else:
        res = {}
        res['resultado'] = "op2 não informado"
        return JsonResponse(res)
        
    res = {}
    res['resultado'] = float(op1) + float(op2)
    return JsonResponse(res)

@require_GET
def sub(request):
    op1 = request.GET.get("op1", "")
    if op1:
        print(f"{op1}")
    else:
        res = {}
        res['resultado'] = "op1 não informado"
        return JsonResponse(res)
            
    op2 = request.GET.get("op2", "")
    if op2:
        print(f"{op2}")
    else:
        res = {}
        res['resultado'] = "op2 não informado"
        return JsonResponse(res)
            
    res = {}
    res['resultado'] = float(op1) - float(op2)
    return JsonResponse(res)
