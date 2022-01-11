from .serializers import  UpdateImageSerializer, showProfileSerializer
from rest_framework.generics import (CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, get_object_or_404)
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import (
	IsAuthenticated,
	IsAuthenticatedOrReadOnly,
	)
from .permissions import IsOwnerOrReadOnly
from blog.models import Profile


# class ImageCreateAPIView(CreateAPIView):
# 	serializer_class = imageSerializer
# 	queryset = Profile.objects.all()

class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Profile.objects.all()
	serializer_class = UpdateImageSerializer
	# lookup_field = 'id'
	# permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(queryset, user=self.request.user)
		return obj

class ShowProfilePhoto(RetrieveAPIView):
	queryset = Profile.objects.all()
	serializer_class = showProfileSerializer
	# lookup_field = 'username'#it must be pk
	authentication_classes = (TokenAuthentication, SessionAuthentication)

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(queryset, user=self.request.user)
		return obj
