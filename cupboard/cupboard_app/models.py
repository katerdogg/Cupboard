"""Models for Cupboard Project"""

from django.db import models

class Cup_User(models.Model):
	"""Holds all data for the user"""
	# avatar = 
	name = models.CharField(max_length=200)

class Fav_Recipe(models.Model):
	"""Holds all Fav Recipe data"""
	# recipe =
	# description = 
	# user_note =


class Fav_Search(models.Model):
	"""Holds all Fav Search data"""
	# search_terms = 
	# user_note =