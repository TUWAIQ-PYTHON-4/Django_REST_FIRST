from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from datetime import date
import  random
from rest_framework import status


# Create your views here.
@api_view(['GET'])
def get_date(request: Request):
    today= date.today()
    str(today)
    data = {"date" : 'Today is {} !'.format(today)}
    return Response(data)

@api_view(["POST"])
def rando(request: Request):

    minum=request.data.get("min",None)
    maxnum=request.data.get("max", None)
    
    randnum= random.randint(minum, maxnum)
    
    if minum>0:
        data = { "random" : randnum }
    else:
        data = {"msg", "Not Allowed. Please provide a min that is bigger than 0"}

    return Response(data, status=status.HTTP_400_BAD_REQUEST)
