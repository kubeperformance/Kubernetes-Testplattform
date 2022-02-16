# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this



urlpatterns = [
 
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path('admin/', admin.site.urls),   
    path("", include("apps.test_service.urls")),       
    path("", include("apps.app.urls")),     
    
           # Django admin route
    
    # UI Kits Html files, Includes core urls (root url)
    
]
