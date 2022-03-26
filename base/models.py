# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Listing(models.Model):
	lister = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)
	item = models.CharField(max_length=200)
	item_amount = models.FloatField()
	item_amount_unit = models.CharField(max_length=10)
	item_expiration_date = models.DateTimeField()
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-updated", "-created"]

	def __str__(self):
		return self.title
