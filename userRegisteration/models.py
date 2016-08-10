from django.db import models

class Users(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	isAgree = models.BooleanField(default=False)