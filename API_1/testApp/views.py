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
    x = str(datetime.date.today())
    print(x)
    today_date = {
        'date': 'Today is ' + x
    }
    return Response(today_date)


@api_view(['POST'])
def random_number(request: Request):
    max_n = request.data.get('max', 0)
    min_n = request.data.get('min', 0)

    if min_n <= 0:
        context = {"msg", "Not Allowed. Please provide a min that is bigger than 0"}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    else:
        res = random.randint(min_n, max_n)
        random_num = {
            'random number': res
        }
        return Response(random_num)
