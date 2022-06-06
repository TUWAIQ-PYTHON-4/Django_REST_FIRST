from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework import status

import datetime
import random

# Create your views here.
@api_view(["GET"])
def Date(request: Request):

    today = str(datetime.datetime.today())
    data = {
        "date" : 'Today is ' +today + '!'
    }

    return Response(data)
   
@api_view(["POST"])
def Random(request: Request):
    
    min = request.data.get("min", None)
    max = request.data.get("max", None)
    rand_num = random.randrange(min, max)
    if min < 0:
        msg = {"msg": "invalid, must be greater than 0"}
        return Response(msg, status= status.HTTP_400_BAD_REQUEST)

    else:
        data = {
            "Random" : rand_num
        }
        return Response(data, status= status.HTTP_200_OK)




