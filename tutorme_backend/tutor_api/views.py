import django_filters

from django.shortcuts import render

from rest_framework import generics, filters

from tutor_api.models import School, User, Class, Department

from tutor_api.serializers import SchoolSerializer, UserSerializer, ClassSerializer, DepartmentSerializer

# Create your views here.

class SchoolList(generics.ListCreateAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer
	filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter)
	filter_fields = ('name', 'zipCode')
	ordering_fields = '__all__'
	ordering = ('id')

class SchoolDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer
	filter_backends = (filters.DjangoFilterBackend,)

class ClassList(generics.ListCreateAPIView):
	queryset = Class.objects.all()
	serializer_class = ClassSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('number', 'major')
	ordering_fields = '__all__'
	ordering = ('id')

class ClassDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Class.objects.all()
	serializer_class = ClassSerializer
	filter_backends = (filters.DjangoFilterBackend,)

class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('name', 'email','phone')
	ordering_fields = '__all__'
	ordering = ('id')

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	filter_backends = (filters.DjangoFilterBackend,)

class DepartmentList(generics.ListCreateAPIView):
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer
	lookup_field = "shortName"
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('name', 'shortName')
	ordering_fields = '__all__'
	ordering = ('id')

class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer
	lookup_field = "shortName"
	filter_backends = (filters.DjangoFilterBackend,)

