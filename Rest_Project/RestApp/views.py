from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
import datetime
import random


# Create your views here.

@api_view(['GET'])
def date(request: Request):
    d = str(datetime.date.today())
    data = {
        "date": "Today is " + d
    }
    return Response(data)


@api_view(["POST"])
def random_num(request: Request):
    mini = request.data.get("min", 0)
    maxi = request.data.get("max", 0)

    if mini <= 0:
        msg = {
            "msg": "Not Allowed. Please provide a min that is bigger than 0"
        }
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)

    else:

        result = random.randint(mini, maxi)
        data = {
            "Random": result
        }
        return Response(data)


