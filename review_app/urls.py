from django.urls import path
from .views import home, kyp

urlpatterns = [
    path('', home, name='home'),
    path('kyp/', kyp, name='kyp'),
]
