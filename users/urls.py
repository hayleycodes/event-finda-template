from django.conf.urls import url
from django.contrib import admin
# from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]