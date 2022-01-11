"""mac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include('shop.urls')),
    path('admin/', admin.site.urls),
    url(r'^shop/', include(('shop.urls', 'shop'), namespace='shop')),
    url(r'^blog/', include(('blog.urls', 'blog'), namespace='blog')),
    # path('shop/', include('shop.urls')),
    # path('blog/', include('blog.urls'))
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <-- social_django

    url(r'^android/', include(('android.urls', 'android'), namespace='android')),#for restframework

    url(r'^image/', include('image_app.urls')),


]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
