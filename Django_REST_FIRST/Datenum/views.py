import datetime

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
import random
@api_view(['GET'])
def mydate(request: Request):
    data = {
        "date": datetime.date.today()
    }

    return Response(data)


@api_view(["POST"])
def get_random(request: Request):
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
            "randomNum": result
        }
        return Response(data)

#   randomNum = random.randint(min, max)
