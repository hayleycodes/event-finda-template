"""eventFinderProject URL Configuration

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
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views
from eventFinderApp import viewsets as EventViewSets
from users import viewsets as UserViewsets

router = routers.DefaultRouter()
router.register(r'events', EventViewSets.EventsViewSet)
router.register(r'users', UserViewsets.CustomUserViewSet)

urlpatterns = [
    path(r'', include('eventFinderApp.urls'), name='eventFinderApp'),
    path('users/', include('users.urls'), name='users'),
    path('users/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', views.obtain_auth_token),
]
