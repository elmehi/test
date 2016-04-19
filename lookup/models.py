from __future__ import unicode_literals
import django
from django.db import models
import datetime

# A source model.
class Source(models.Model):
    source_quote = models.TextField()
    source_url = models.CharField(max_length = 200)
    source_title = models.CharField(max_length = 200)
    source_name = models.CharField(max_length = 200)
    source_date = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.source_quote

class User(models.Model):
	username = models.CharField(max_length = 200)
	password = models.CharField(max_length = 20)
	highlight_url = models.BooleanField(default = True)
	date_created = models.DateTimeField(default=django.utils.timezone.now)

	def __str__(self):
		return self.username

class Request(models.Model):
	user_id = models.BigIntegerField()
	request_date = models.DateTimeField(default=django.utils.timezone.now)
	request_source = models.ForeignKey('Source', on_delete=models.DO_NOTHING)
