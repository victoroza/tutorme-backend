from rest_framework import serializers

from tutor_api.models import School, User, Class, Department

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = School
		fields = ('id', 'created', 'name', 'zipCode')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		print "HERE1"
		model = User
		fields = ('id', 'created', 'first_name', 'last_name', 'is_staff', 
			'is_active', 'is_superuser','email', 'phone', 'password', 'username')
		# extra_kwargs = {'password': {'write_only': True}}
	# def update(self, attrs, instance=None):
	# 	print type(attrs);
	# 	password = attrs.pop('password', None)

	# 	if instance:
	# 	# Update an existing customer
	# 		for key, val in attrs:
	# 			setattr(user, key, val)
	# 	else:
	# 	# Create a new customer
	# 		user = User(**attrs)
	# 	if password:
	# 		user.set_password(password)

	# 	user.save()
	# 	return user
	def create(self, validated_data):
		print 'here'
		user = User(**validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user
	def update(self, instance, validated_data):
		instance.first_name = validated_data.get('first_name', instance.first_name)
		return user

class ClassSerializer(serializers.ModelSerializer):
	# major = serializers.HyperlinkedRelatedField(queryset=Department.objects.all(), read_only=False, view_name='department-detail', lookup_field='shortName')
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

# class AppointmentSerializer(serializers.)
