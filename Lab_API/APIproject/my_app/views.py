import random
from datetime import datetime
from os import stat
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def date_today(request : Request):
    current_datetime = datetime.now()
    date ={"date": " Today is "+str(current_datetime)
    }
    return Response(date)

@api_view(['POST'])
def randome_number(request : Request):
    min = request.data.get("min",None)
    max = request.data.get("max", None)
    ran_num = random.randrange(min, max)
    if min <0:
        m ={"msg":"Not Allowed. Please provide a min that is bigger than 0"}
        return Response(m, status=status.HTTP_400_BAD_REQUEST)
    data ={"max :" : max ,
           "min:" : min ,
            "random:" : ran_num}
    #random_num = {"random:":random.randint(min, max)}
    return Response(data)


