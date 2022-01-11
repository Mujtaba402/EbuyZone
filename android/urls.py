
from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken import views as tokenview
from . import views



urlpatterns = [
    path('api-token-auth/', tokenview.obtain_auth_token, name='api-token-auth'),
    url(r'^orders/$', views.PostListAPIView.as_view(), name='restpost-list'),
    url(r'^orders/(?P<order_id>[\w-]+)/$', views.ShowPost.as_view(), name='restpost-show'),
    url(r'^orders/delete/(?P<order_id>[\w-]+)/$', views.DeletePost.as_view(), name='delete'),
    url(r'^order_status/$', views.AddOrderDelivered.as_view(), name='add'),# for add serializer url should contain one /
    url(r'^profile/(?P<username>[\w-]+)/$', views.ShowProfile.as_view(), name='show_profile'),
]