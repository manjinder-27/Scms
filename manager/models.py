from django.db import models

# Create your models here.
class Student(models.Model):
	admNum = models.CharField(max_length=30,null=True)
	firstName = models.CharField(max_length=30,null=True)
	lastName = models.CharField(max_length=30,null=True)
	fatherName = models.CharField(max_length=30,null=True)
	phoneNumber = models.CharField(max_length=13,null=True)
	studentClass = models.CharField(max_length=30,null=True)
	
	def __str__(self):
		return self.firstName



class Application(models.Model):
	appId = models.CharField(max_length=30,null=True)
	firstName = models.CharField(max_length=30,null=True)
	lastName = models.CharField(max_length=30,null=True)
	fatherName = models.CharField(max_length=30,null=True)
	phoneNumber = models.CharField(max_length=13,null=True)
	studentClass = models.CharField(max_length=30,null=True)
	
	def __str__(self):
		return self.firstName