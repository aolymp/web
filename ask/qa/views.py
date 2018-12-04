from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
def test(request, *args, **kwargs):
	return HttpResponse('OK')

def login(request, *args, **kwargs):
	return HttpResponse('User')

def question(request, uid):
    return HttpResponse(uid)

