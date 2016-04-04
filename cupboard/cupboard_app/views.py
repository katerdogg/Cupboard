""" views for cupboard capstone """
from django.shortcuts import render
import requests
import json
from yummly import Client

# Create your views here.

def index(request):
	return render(request, "cupboard_app/index.html")

def search(request):
	return render(request, "cupboard_app/search.html")

def results(request):
	context_dict = {}
	if request.method == "POST":
		search_list = request.POST["ingredients"].split(", ")
		client = Client(api_id="243f40b9", api_key="0b99d35c38f2043e163a04a97e9c5476", timeout=5.0, retries=0)
		params = {
	    'q': search_list,
	    'start': 0,
	    # 'maxResult': 40,
	    # 'requirePicutres': True,
	    # 'allowedIngredient[]': ['salt', 'pepper'],
	    # 'excludedIngredient[]': ['cumin', 'paprika'],
	    'maxTotalTimeInSeconds': 3600,
	    # 'facetField[]': ['ingredient', 'diet'],
	    # 'flavor.meaty.min': 0.5,
	    # 'flavor.meaty.max': 1,
	    # 'flavor.sweet.min': 0,
	    # 'flavor.sweet.max': 0.5,
	    # 'nutrition.FAT.min': 0,
	    # 'nutrition.FAT.max': 15,
		}
		results = client.search(**params)
		context_dict = {"results": results.matches}
	
	return render(request, "cupboard_app/results.html", context_dict)
