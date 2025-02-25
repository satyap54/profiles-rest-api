from rest_framework import serializers

from . import models

class HelloSerializer(serializers.Serializer):
	"""Serializes a name field for testing out APIView"""
	name = serializers.CharField(max_length=10)


""" Model Serializer for User Profiles """
class UserProfileSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = models.UserProfile
		fields = ('id', 'email', 'name', 'password')
		extra_kwargs = {
			'password' : {
				'write_only' : True,
				'style' : {'input_type' : 'password'}
			}
		}


	def create(self, validated_data):
		user = models.UserProfile.objects.create_user(
			email = validated_data['email'],
			name = validated_data['name'],
			password = validated_data['password'],
		)

		return user

	def update(self, instance, validated_data):
		"""Handle updating user account"""
		if 'password' in validated_data:
			password = validated_data.pop('password')
			instance.set_password(password)
 
		return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
	""" Serializes profile feel items """

	class Meta:
		model = models.ProfileFeedItem
		fields = ('id', 'user_profile', 'status_text', 'created_on')
		read_only_fields = ['user_profile']