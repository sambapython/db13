from django.db import models

"""
create table gateway(name varchar(250))
"""

# Create your models here.
class Gateway(models.Model):
	name = models.CharField(max_length=300) # blank=True, null=True, unique=True, primary_key=True
	ip = models.GenericIPAddressField()
	mask = models.GenericIPAddressField()
	route = models.GenericIPAddressField()
	interface_name=models.CharField(max_length=300)
