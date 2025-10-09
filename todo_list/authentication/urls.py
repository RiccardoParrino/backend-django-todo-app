from django.urls import path
from . import views

urlpatterns = [
    path('login',view=views.login, name='pair'),
    path('createUser', view=views.create_user, name='refresh'),
    path('listAllUser', view=views.list_all_users, name='list_all_users')
]