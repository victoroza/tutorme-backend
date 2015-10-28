from rest_framework import serializers

from tutor_api.models import School, User, Class, Department

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = School
		fields = ('id', 'created', 'name', 'zipCode')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'created', 'name', 'email', 'phone')

class ClassSerializer(serializers.HyperlinkedModelSerializer):
	major = serializers.HyperlinkedRelatedField(queryset=Department.objects.all(), read_only=False, view_name='department-detail', lookup_field='shortName')
	# school = serializers.HyperlinkedRelatedField(read_only=True, view_name='school-detail')
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
