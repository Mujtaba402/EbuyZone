from rest_framework import serializers

from rest_framework.serializers import (
      ModelSerializer,
)

from blog.models import Profile


class UpdateImageSerializer(ModelSerializer):
   class Meta:
      model = Profile
      fields = [
         'photo',
      ]

class showProfileSerializer(ModelSerializer):
	class Meta:
		model = Profile
		fields = (
           'id',
           'photo',
		)