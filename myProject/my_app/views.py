from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from datetime import date
import random

# Create your views here.

@api_view(['GET'])
def get_today_date(request: Request):
    today = date.today()

    data = {
        "Today's date": today
    }

    return Response(data)

@api_view(["POST"])
def random_number(request: Request):
    min=request.data.get("min")
    max=request.data.get("max")



    data = {
        "random" : random.randint(min,max)

    }
    if min > 0:
        return Response(data, status=status.HTTP_200_OK)
    else:
        data = {
            "msg", "Not Allowed. Please insert value bigger than 0"}


    return Response(data, status=status.HTTP_400_BAD_REQUEST)