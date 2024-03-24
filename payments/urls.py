from django.urls import path

from payments.apps import PaymentsConfig

from payments.views import PaymentsListAPIView, SubscribeCreateAPIView, PaymentsCreateAPIView, PaymentStatusAPIView, \
    PaymentsRetrieveAPIView

app_name = PaymentsConfig.name


urlpatterns = [
    path('list/', PaymentsListAPIView.as_view(), name='payment_list'),
    path('subscribe/', SubscribeCreateAPIView.as_view(), name='subscribe'),
    path('create/', PaymentsCreateAPIView.as_view(), name='payments_create'),
    path('status/', PaymentStatusAPIView.as_view(), name='payments_status'),
    path('payment/<int:pk>/', PaymentsRetrieveAPIView.as_view(), name='payments_detail')
              ]
