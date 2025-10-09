from django.urls import path
from rest_framework_simplejwt import views

urlpatterns = [
    # path('pair', views.pair, name='pair'),
    # path('refresh', views.refresh, name='refresh'),
    # path('verify', views.verify, name='verify'),
    path('django', views.TokenObtainPairView.as_view(), name='django_token_pair_view')
]