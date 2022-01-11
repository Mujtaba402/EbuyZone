from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="bloghome"),
    path("blogpost/<int:id>", views.blogPost, name="blogPost"),
    url(r'edit_profile/$', views.editProfile, name="edit_profile"),
]