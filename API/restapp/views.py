import datetime, random
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

@api_view(['GET'])
def date(request: Request):
    current_datetime = datetime.datetime.now()
    data = {
        "current_datetime": f"Today is {current_datetime}for today..!"
    }

    return Response(data)


@api_view(["POST"])
def random_number(request: Request):
    min1 = request.data.get("min1", None)
    max1 = request.data.get("max1", None)
    if min1 < 0:
        data = {
            "msg": "a response that it is not supported"
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    else:
        rand = random.randrange(min1, max1)
        data = {
            "rand": rand
        }
        return Response(data, status=status.HTTP_200_OK)
