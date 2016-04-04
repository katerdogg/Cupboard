"""
views for cupboard capstone
"""

### IMPORTS ###
from django.shortcuts import render
import requests
import json
from yummly import Client
###############

def index(request):
	return render(request, "cupboard_app/index.html")

def search(request):
	return render(request, "cupboard_app/search.html")

def results(request):
	"""
	Results page for the search from the user
	"""
	context_dict = {}
	# If requested (if the submit button has been clicked)
	if request.method == "POST":
		# var to hold the ingredients entered into the form on the search page; split each ingredient by
			# a comma and a space
		search_list = request.POST["ingredients"].split(", ")
		# var to hold the api id and key
		client = Client(api_id="243f40b9", api_key="0b99d35c38f2043e163a04a97e9c5476", timeout=5.0, retries=0)
		
		# parameters for each search.
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
		# var results to hold the client search parameters; **params to hold as many or as few as it needs
		results = client.search(**params)
		# var context_dict to hold a dictionary of each result match with the key "results"
		context_dict = {"results": results.matches}

	return render(request, "cupboard_app/results.html", context_dict)
