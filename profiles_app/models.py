from django.db import models
from django.shortcuts import get_object_or_404


# Create your models here.

class Stream(models.Model):
	name = models.CharField(max_length=40)

	def __str__(self):
		return self.name



class College(models.Model):
	name = models.CharField(max_length=50)
	city = models.CharField(max_length=20)
	streams = models.ManyToManyField(Stream, related_name='in_colleges')


	def __str__(self):
		return self.name

	




class Student(models.Model):
	full_name = models.CharField(max_length=25)
	email = models.EmailField(unique=True)
	mob_no = models.IntegerField(unique=True)
	college = models.ForeignKey(College, null=False, related_name='students', on_delete=models.CASCADE)
	stream = models.ForeignKey(Stream, null=False, related_name='students', on_delete=models.CASCADE)

	def __str__(self):
		return self.full_name + ", " + self.college.name
