import django_filters

from rest_framework import generics, filters

from tutor_api.models import School, User, Class, Department, Appointment

from tutor_api.serializers import SchoolSerializer, UserSerializer, ClassSerializer, DepartmentSerializer, AppointmentSerializer

# Create your views here.

class SchoolList(generics.ListCreateAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer
	filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
	filter_fields = ('id', 'name', 'zipCode')
	ordering_fields = '__all__'
	ordering = ('id')
	search_fields= ('name','zipCode')

class SchoolDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer

class ClassList(generics.ListCreateAPIView):
	queryset = Class.objects.all()
	serializer_class = ClassSerializer
	filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
	filter_fields = ('id','number', 'major__shortName','school__name')
	ordering_fields = '__all__'
	ordering = ('id')
	search_fields= ('number','major__shortName', 'school__name')

class ClassDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Class.objects.all()
	serializer_class = ClassSerializer

class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	lookup_field = "username"
	filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
	filter_fields = ('id', 'first_name', 'last_name','phone', 'email', 'username')
	ordering_fields = '__all__'
	ordering = ('id')
	search_fields= ('first_name','email', 'phone', 'last_name', 'username')


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	lookup_field = "username"


class DepartmentList(generics.ListCreateAPIView):
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer
	lookup_field = "shortName"
	filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
	filter_fields = ('name', 'shortName')
	ordering_fields = '__all__'
	ordering = ('id')
	search_fields= ('name','shortName',)

class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer
	lookup_field = "shortName"

class AppointmentList(generics.ListCreateAPIView):
	queryset = Appointment.objects.all()
	serializer_class = AppointmentSerializer
	filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
	filter_fields = ('id', 'aClass__number', 'tutee__username', 'tutor__username', 'time', 'location', 'notes')
	ordering_fields = '__all__'
	ordering = ('id')
	search_fields= ('aClass__number', 'tutee__username', 'tutor__username', 'time', 'location', 'notes')

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Appointment.objects.all()
	serializer_class = AppointmentSerializer
