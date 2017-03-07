from django.shortcuts import render
from django.http import HttpResponse
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core import serializers
from django.http import JsonResponse
import random



def home(request):
	return render(request,"main/index.html",{})




def qalam(request):
	return render(request,"main/qalam.html",{})




def gozine(request):
	return render(request,"main/gozine.html",{})

