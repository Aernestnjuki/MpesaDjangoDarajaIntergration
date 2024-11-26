from django.urls import path
from . import views

urlpatterns = [
    path('', views.MpesaIndexAPIView.as_view(), name='index'),
    path('daraja/stk-push/', views.StkPushCallbackAPIView.as_view(), name='mpesa-stk-push-callback')
]
