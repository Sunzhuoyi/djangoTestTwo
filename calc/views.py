# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a)+int(b)
	return HttpResponse(str(c))
def add2(request,a,b):
	c = int(a) + int(b)
	return HttpResponse(str(c))
def index(request):
	return render(request, 'home.html')
def old_add2_redirect(request,a,b):
	return HttpResponseRedirect(
		reverse('add2',args=(a,b))
		)

# Create your views here.
