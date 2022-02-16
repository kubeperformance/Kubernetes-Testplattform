# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path, include
from django.contrib import admin
from apps.app import views
from rest_framework import routers




router = routers.SimpleRouter()
router.register(r'tests', views.TestViewSet)

# Webapp Patterns
urlpatterns = [
    
    
    # The home page
    path('', views.index, name='home'),    
    path('', include(router.urls)),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]


#REST URLs


