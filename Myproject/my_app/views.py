from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from datetime import date
import random

# Create your views here.

@api_view(['GET'])
def get_date(request: Request):
    today = date.today()

    data = {
        "Today's date": today
    }

    return Response(data)


@api_view(['POST'])
def add_random(request : Request):
    min = request.data.get('min', 0)
    max = request.data.get('max', 0)
    random_num= random.randint(min,max)
    if min < 0:
       data = {
            "msg": "Not Allowed. Please provide a min that is bigger than 0"
            }
       return Response(data, status=status.HTTP_400_BAD_REQUEST)

    else:

        data = {

            "min": min,
            "max": max,
            "random": random_num
        }
        return Response(data)

