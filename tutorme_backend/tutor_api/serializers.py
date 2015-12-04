from rest_framework import serializers

from tutor_api.models import School, User, Class, Department, Appointment, Tutor

from django.contrib.auth.hashers import make_password

from django.http import HttpResponse
from django.core.exceptions import ValidationError

from rest_framework.response import Response

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = School
		fields = ('id', 'created', 'name', 'zipCode')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'created', 'first_name', 'last_name', 'is_staff', 
			'is_active', 'is_superuser','email', 'phone', 'password', 'username')
		lookup_field = 'username'
		extra_kwargs = {'password': {'write_only': True}}
	def create(self, validated_data):
		user = User(**validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user
	def update(self, instance, validated_data):
		temp = instance
		instance.first_name = validated_data.get('first_name', instance.first_name)
		instance.last_name = validated_data.get('last_name', instance.last_name)
		instance.is_staff = validated_data.get('is_staff', instance.is_staff)
		instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
		instance.is_active = validated_data.get('is_active', instance.is_active)
		instance.email = validated_data.get('email', instance.email)
		instance.phone = validated_data.get('phone', instance.phone)
		instance.username = validated_data.get('username', instance.username)
		# instance.password = make_password(validated_data.get('password', instance.first_name))
		instance.password = instance.password
		user = User.objects.get(username=instance.username)
		if(user.check_password(str(validated_data.get('password')))):
			instance.save()
		else:
			instance=temp
			# return Response({
			# 	'password': 'The password was incorrect.'
			# }, status=401)
			# raise ValidationError({
			# 	'password': 'The password was incorrect.'
			# })
		return instance

class ClassSerializer(serializers.ModelSerializer):
	major = serializers.HyperlinkedRelatedField(queryset=Department.objects.all(), read_only=False, view_name='department-detail', lookup_field='shortName')
	school = serializers.HyperlinkedRelatedField(queryset=School.objects.all(), read_only=False, view_name='school-detail')
	class Meta:
		model = Class
		fields = ('id', 'created', 'number', 'major', 'school')
		# extra_kwargs = {
		# 	'major' : {'view_name': 'departments-detail', 'lookup_field': 'shortName'}
		# }

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Department
		fields = ('id', 'shortName', 'name')
		lookup_field = 'shortName'
		# extra_kwargs = {
		# 	'url' : {'view_name': 'department-detail', 'lookup_field': 'shortName'}
		# }

class AppointmentSerializer(serializers.ModelSerializer):
	aClass = serializers.HyperlinkedRelatedField(queryset=Class.objects.all(), read_only=False, view_name='class-detail')
	tutee = serializers.HyperlinkedRelatedField(queryset=User.objects.all(), read_only=False, view_name='user-detail', lookup_field='username')
	tutor = serializers.HyperlinkedRelatedField(queryset=User.objects.all(), read_only=False, view_name='user-detail', lookup_field='username')
	class Meta:
		model = Appointment
		fields = ('id', 'created', 'aClass', 'time', 'location', 'notes',
			'tutor', 'tutee')

class TutorSerializer(serializers.ModelSerializer):
	aClass = serializers.HyperlinkedRelatedField(queryset=Class.objects.all(), read_only=False, view_name='class-detail')
	user = serializers.HyperlinkedRelatedField(queryset=User.objects.all(), read_only=False, view_name='user-detail', lookup_field='username')
	class Meta:
		model = Tutor
		fields = ('id', 'created', 'aClass', 'user')