from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.]
class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=MyUserManager.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        print "HERE"
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        print "HERE"
        user = self.create_user(email,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class School(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.TextField(unique=True)
	zipCode = models.IntegerField()
	picture = models.TextField(default="http://comps.canstockphoto.com/can-stock-photo_csp16035165.jpg")
	def __unicode__(self):
		return self.name

class User(AbstractUser):
	objects = MyUserManager()
	created = models.DateTimeField(auto_now_add=True)
	phone = models.BigIntegerField()
	picture = models.TextField(default="http://previews.123rf.com/images/kritchanut/kritchanut1406/kritchanut140600093/29213195-Male-silhouette-avatar-profile-picture-Stock-Vector-profile.jpg")
	class Meta:
		db_table = 'auth_user'

class Department(models.Model):
	shortName = models.CharField(unique=True, max_length=10)
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.shortName

class Class(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	number = models.IntegerField()
	major = models.ForeignKey(Department, related_name='classes', to_field='shortName')
	school = models.ForeignKey(School, related_name='classes')
	def __unicode__(self):
		return self.major.shortName+str(self.number)+'-'+str(self.school.name)

class Appointment(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	aClass = models.ForeignKey(Class, related_name='appointments')
	tutee = models.ForeignKey(User, related_name='appointments_tutee', to_field='username')
	tutor = models.ForeignKey(User, related_name='appointments_tutor', to_field='username')
	time = models.DateTimeField()
	location = models.TextField()
	notes = models.TextField()

class Tutor(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	aClass = models.ForeignKey(Class, related_name='tutoring')
	user = models.ForeignKey(User, related_name='tutoring', to_field='username')