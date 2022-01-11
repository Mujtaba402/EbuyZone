from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import JsonResponse

from .serializers import (
	showProfileSerializer,
	listSerializer,
	deleteSerializer,
	addSerializer,
	showSerializer,
	)

from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView,
									 get_object_or_404)

from shop.models import OrderReceived, OrderCome
from blog.models import Profile


from rest_framework.permissions import (
	IsAuthenticated,
	)
from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication

class PostListAPIView(ListAPIView):
	serializer_class = listSerializer
	queryset = OrderReceived.objects.all()

class ShowPost(RetrieveAPIView):
	queryset = OrderReceived.objects.all()
	serializer_class = showSerializer
	lookup_field = 'order_id'#it must be pk

class DeletePost(DestroyAPIView):
	queryset = OrderReceived.objects.all()
	serializer_class = deleteSerializer
	lookup_field = 'order_id'#it must be pk
	authentication_classes = (TokenAuthentication, SessionAuthentication)

class AddOrderDelivered(CreateAPIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	serializer_class = addSerializer
	queryset = OrderCome.objects.all()

class ShowProfile(RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = showProfileSerializer
	lookup_field = 'username'#it must be pk





