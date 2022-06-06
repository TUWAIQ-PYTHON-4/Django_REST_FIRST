from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
import datetime
from random import randint

# Create your views here.


@api_view(['GET'])
def date (request: Response) :
    
    date = {

        'date' : "Todyis" + str(datetime.date.today())
    }

    return Response (date)


@api_view(["POST"])
def random (request: Request):


    min_num = request.data.get ('min' , None)
    max_num = request.data.get('max' , None)
    random_num = randint(min_num,max_num)

    if min_num < 0 :
        data = {

            'masseg' : ' Not allowed '
        }
    
        return Response (data)
    
    data = {

        'Your number': str(max_num) + "to" + str(min_num),
        ' random number' : random_num
    }

    return Response (data)