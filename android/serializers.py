from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
)
from shop.models import OrderReceived, OrderCome
from django.contrib.auth.models import User


class listSerializer(ModelSerializer):
	class Meta:
		model = OrderReceived
		# fields = [
		# 	'id',
		# 	'category',
		# 	'title',
		# 	'text',
		# ]

		fields = [
			'order_id',
			'address',
			'name',

		]

class showSerializer(ModelSerializer):
	class Meta:
		model = OrderReceived
		fields = [
			'order_id',
			'items_details',
			'name',
		]

class deleteSerializer(ModelSerializer):
	class Meta:
		model = OrderReceived
		fields = [
			'order_id',
		]

class addSerializer(ModelSerializer):
	class Meta:
		model = OrderCome
		fields = [
			'order_id',
			'update_desc',
		]

class showProfileSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = (
			'username',
			'email',
			'first_name',
			'last_name',
		)
