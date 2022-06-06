from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
import datetime
from random import randint


@api_view(['GET'])
def date(request: Request):
    today = datetime.datetime.today()
    today = str(today)
    data = {"date": "Today is "+today+" !"}
    return Response(data)

@api_view(['POST'])
def randomview(request : Request):

    number_one = request.data.get("min", None)
    number_two = request.data.get("max", None)
    if number_one < 0 :
        data = {"msg", "Not Allowed. Please provide a min that is bigger than 0"}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    else:
        random_number = randint(number_one,number_two)
        data = {"random": random_number}
        return Response(data, status=status.HTTP_200_OK)