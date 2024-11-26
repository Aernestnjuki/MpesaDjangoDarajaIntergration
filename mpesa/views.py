from django.shortcuts import render
from rest_framework.response import Response
from django_daraja.mpesa.core import MpesaClient
from rest_framework.views import APIView

class MpesaIndexAPIView(APIView):
    def post(self, request, *args, **kwargs):
        c1 = MpesaClient()
        phone_number = '0705203169'
        amount = 1
        account_reference = 'reference'
        transaction_desc = 'Description'
        callback_url = 'https://darajambili.herokuapp.com/express-payment'
        response = c1.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        return Response(response)
    

class StkPushCallbackAPIView(APIView):
    def get(self, request):
        data = request.body
        return Response({'data': data})
