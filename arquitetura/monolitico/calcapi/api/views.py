from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def calc(request):
    res = {}
    res['resultado'] = "calc está funcionando! Versão 1.0"
    return JsonResponse(res)  

def soma(request):
    pass


