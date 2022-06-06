from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from random import randrange

@api_view(["GET"])
def index(request: Request):

    data = {

        "date": "Today is 2022-06-06 !"
    }
    return Response(data)

@api_view(["POST"])
def random(request: Request):


    minn = request.data.get("min", None)
    max = request.data.get("max", None)
    max_val : int = request.data.get("max_val", None)
    min_val : int = request.data.get("min_val", None)

    random = randrange(max_val,min_val)

    if min_val < 0 :
        data = {
            'msg': "Not Allowed. Please provide a min that is bigger than 0"
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    else:
        random = randrange(min_val, max_val)
        data = {
             "random num": random
        }
        return Response(data, status=status.HTTP_200_OK)

   
