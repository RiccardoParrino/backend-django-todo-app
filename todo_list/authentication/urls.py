from django.urls import path
from . import views

urlpatterns = [
    path('login',view=views.login, name='pair'),
    path('createUser', view=views.create_user, name='refresh'),
]