from os import stat
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from datetime import date
from random import randint

@api_view(['GET'])
def date(request : Request):
    data = {
        "date" : f"Today is {date.today()}"
    }

    return Response(data)

@api_view(["POST"])
def random(request: Request):

    min =  request.data.get("min", None)
    max = request.data.get('max', None)

    random = randint(min, max)

    data = {
        "random" : random
    }


    return Response(data, status=status.HTTP_200_OK)

