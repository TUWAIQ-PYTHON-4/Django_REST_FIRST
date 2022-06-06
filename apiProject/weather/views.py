from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def date(request: Request):
    from datetime import date
    data = {
        "date": "Today is {}".format(date.today())

    }
    return Response(data)


@api_view(["POST"])
def random(request: Request):
    import random

    min_num: int = request.data.get("min_num", None)
    max_num: int = request.data.get("max_num", None)

    if min_num < 0:
        data = {
            "msg": "Not Allowed. Please provide a min that is bigger than 0"
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    else:
        random_num = random.randint(min_num, max_num)
        data = {
            "random num": random_num
        }

        return Response(data, status=status.HTTP_200_OK)
