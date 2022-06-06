import datetime
from random import randint, random
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from os import stat


@api_view(['GET'])
def date(request : Request):
    data = {
       "date" : datetime.date.today()
    }
    return Response(data)



@api_view(['POST'])
def random(request: Request):
    min = request.data.get('min',None)
    max = request.data.get("max",None)
    random1 = randint(min, max)
    if min < 0:
        data = {
        "msg" : "Not Allowed. Please provide a min that is bigger than 0"
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    max = request.data.get("max",None)
    random1 = randint(min, max)
    print(random1)
    data = {
        "Random numbers genrates" : str(min) + " to " + str(max),
        "Random number genrated" : random1
    }
    return Response(data, status=status.HTTP_200_OK)