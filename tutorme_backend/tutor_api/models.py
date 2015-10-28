from django.db import models

# Create your models here.]

class School(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.TextField()
	zipCode = models.IntegerField()
	def __unicode__(self):
		return self.name


class User(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=254)
	phone = models.IntegerField()

class Department(models.Model):
	shortName = models.CharField(unique=True, max_length=10)
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.shortName

class Class(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	number = models.IntegerField()
	major = models.OneToOneField(Department, related_name='classes')
	school = models.OneToOneField(School, related_name='classes')

