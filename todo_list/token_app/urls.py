from django.urls import path
from . import views

urlpatterns = [
    # path('pair', views.pair, name='pair'),
    # path('refresh', views.refresh, name='refresh'),
    # path('verify', views.verify, name='verify'),
    path('django', views.MyTokenObtainPairView.as_view(), name='django_token_pair_view')
]