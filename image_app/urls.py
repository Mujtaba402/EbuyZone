from django.conf.urls import include, url
from . import views

urlpatterns = [
    # url(r'^upload/$', ImageCreateAPIView.as_view()),
    url(r'^editPhoto/$', views.PostUpdateAPIView.as_view(), name='edit'),
    url(r'^showPhoto/$', views.ShowProfilePhoto.as_view(), name='edit'),
]