from django.db import models

"""
create table gateway(name varchar(250))
"""

# Create your models here.
class CommonFieldsModel(models.Model):
	"""
	This is an abstract model. when you migrate for this model no table created in the database.
	we will use this to reduce the number of column statements in the models.
	"""
	name = models.CharField(max_length=300) # blank=True, null=True, unique=True, primary_key=True
	mask = models.GenericIPAddressField()
	create_date = models.DateTimeField(auto_now_add=True)
	class Meta:
		abstract=True

class Gateway(CommonFieldsModel):
	ip = models.GenericIPAddressField(unique=True)
	route = models.GenericIPAddressField()
	interface_name=models.CharField(max_length=300)

	def __str__(self):
		return self.name


class Vlan(models.Model):
	number = models.IntegerField()
	gateway = models.ForeignKey(Gateway, on_delete = models.PROTECT) 


class Switch(CommonFieldsModel):
    valns = models.ManyToManyField(Vlan,blank=True, null=True)
    manamentip = models.GenericIPAddressField()
    


