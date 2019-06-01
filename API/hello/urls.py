from rest_framework.authtoken import views as authviews
from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from hello import views

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/


urlpatterns = [
    url(r'^client/$', views.AllPost.as_view()),
    path("api-toke-auth/", authviews.obtain_auth_token)
]
