from django.db import models



class CompanyModel(models.Model):

	objects=models.Manager()

	information=models.TextField(null=True,blank=True)

	class Meta:
		db_table='CompanyDBTable'

	# def __str__(self):
	# 	return 'owner:'+str(self.owner)