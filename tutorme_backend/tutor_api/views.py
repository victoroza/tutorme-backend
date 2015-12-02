import django_filters

from rest_framework import generics, filters

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
	filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
	filter_fields = ('first_name', 'email','phone')
	ordering_fields = '__all__'
	ordering = ('id')
	search_fields= ('first_name','email', 'phone')
	# def pre_save(self, obj):
	# 	print "CALLED"
	# 	obj.password = make_password(obj.password)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	# def pre_save(self, obj):
	# 	print "CALLED"
	# 	obj.password = make_password(obj.password)

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
	filter_backends = (filters.DjangoFilterBackend,)

class DepartmentList(generics.ListCreateAPIView):
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer
	lookup_field = "shortName"

class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer
	lookup_field = "shortName"

