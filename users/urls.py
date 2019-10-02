from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # users/1
    path('<int:pk>/', login_required(views.AccountView.as_view()), name='account'),
]