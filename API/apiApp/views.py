from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from datetime import date
import random


# Create your views here.
@api_view(['GET'])
def index(request: Request):
    today = date.today()
    data = {'date': today}
    return Response(data)


@api_view(['POST'])
def max_min(request: Request):
    max = request.data.get("max_num", 10)
    min = request.data.get("min_num", -1)
    if min < 0:
        data = {"msg": "Not Allowed. Please provide a min that is bigger than 0"}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    else:
        x = random.randint(min, max)
        data = {"min": min, "max": max, "result": x}
        return Response(data)
