from django.shortcuts import render
from django.conf import settings
from rest_framework.response import Response
from django_daraja.mpesa.core import MpesaClient
from rest_framework.views import APIView
import json

class MpesaIndexAPIView(APIView):
    def post(self, request, *args, **kwargs):
        c1 = MpesaClient()
        phone_number = settings.PHONE_NUMBER
        amount = 1
        account_reference = 'reference'
        transaction_desc = 'Description'
        callback_url = 'https://darajambili.herokuapp.com/express-payment'
        response = c1.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        return Response({"response": response})
    

class StkPushCallbackAPIView(APIView):
    def get(self, request, *args, **kwargs):
        c1 = MpesaClient()
        # data = request.body
        # return c1.parse_stk_result(data)
        result = json.loads(request.body)
        return Response(c1.parse_stk_result(result))
