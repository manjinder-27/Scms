from django.db import models

# Create your models here.
class Student(models.Model):
	adm = models.CharField(max_length=30,null=True)
	name = models.CharField(max_length=30,null=True)
	father = models.CharField(max_length=30,null=True)
	phone = models.CharField(max_length=30,null=True)
	aadhar = models.CharField(max_length=13,null=True)
	cls = models.CharField(max_length=30,null=True)
	
	def __str__(self):
		return self.name


class Employee(models.Model):
	uid = models.CharField(max_length=30,null=True)
	name = models.CharField(max_length=30,null=True)
	father = models.CharField(max_length=30,null=True)
	phone = models.CharField(max_length=30,null=True)
	aadhar = models.CharField(max_length=13,null=True)
	job = models.CharField(max_length=30,null=True)
	
	def __str__(self):
		return self.name


class Application(models.Model):
	name = models.CharField(max_length=30,null=True)
	father = models.CharField(max_length=30,null=True)
	aadhar = models.CharField(max_length=30,null=True)
	phone = models.CharField(max_length=13,null=True)
	appliedFor = models.CharField(max_length=30,null=True)
	appliedAs = models.CharField(max_length=30,null=True)
	
	def __str__(self):
		return self.name