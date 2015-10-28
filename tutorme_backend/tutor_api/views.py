from django.shortcuts import render

from rest_framework import generics

from tutor_api.models import School, User, Class, Department

from tutor_api.serializers import SchoolSerializer, UserSerializer, ClassSerializer, DepartmentSerializer

# Create your views here.

class SchoolList(generics.ListCreateAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer

class SchoolDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer

class ClassList(generics.ListCreateAPIView):
	queryset = Class.objects.all()
	serializer_class = ClassSerializer

class ClassDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Class.objects.all()
	serializer_class = ClassSerializer

class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class DepartmentList(generics.ListCreateAPIView):
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer
	lookup_field = "shortName"

class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer
	lookup_field = "shortName"

