"""
URL configuration for examplesite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

import time

import urllib3
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from polls import views
from polls.tasks import xsumip
from rest_framework import routers


def trigger_error(request):
    division_by_zero = 1 / 0


def get_my_ip(request):
    resp = urllib3.request("GET", "http://ip-api.com/json")
    return HttpResponse(f"Hello from {resp.json()['query']}")


def sum_my_ip(request):
    result = xsumip.delay()
    time.sleep(1)
    while not result.ready():
        time.sleep(1)
    return HttpResponse(f"my ip address sums to {result.get()}")


urlpatterns = [
    path("my-ip/", get_my_ip),
    path("sum-my-ip/", sum_my_ip),
    path("sentry-debug/", trigger_error),
    path("admin/", admin.site.urls),
    path("polls/", include("polls.urls")),
]
