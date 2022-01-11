from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.authtoken import views as tokenview

urlpatterns = [
    path("", views.index, name="shophome"),

    path("about/", views.about, name="aboutus"),
    path("basic/", views.basic, name="basic"),
    path("contact/", views.contact, name="contactus"),
    path("tracker/", views.tracker, name="trackingstatus"),
    path("search/", views.search, name="searchus"),
    # path("productview/<int:myid>", views.productview, name="product"),
    url(r'^productview/(?P<myid>\d+)/$', views.productview, name='productview'),
    path("checkout/", views.checkout, name="check"),
    path("thanks/", views.thanks, name="thanks"),
    path("signup", views.handleSignup, name="handleSignup"),
    path("login", views.handleLogin, name="handleLogin"),
    path("logout", views.handleLogout, name="handleLogout"),
    path("like_post/", views.likePost, name='like_post'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),


    path('api-token-auth/', tokenview.obtain_auth_token, name='api-token-auth'),
]