from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
import random
import datetime

# date view that has API path: my_app/date ['GET']
@api_view(['GET'])
def date(request: Request):
    today = datetime.date.today()
    print(today)
    todays_date = f"Today is  {today}!"

    data = {
        "date": todays_date
    }

    return Response(data)


# random view that has API path : my_app/random ['POST']
@api_view(['POST'])
def random_api(request: Request):
    min = request.data.get('min', None)
    max = request.data.get('max', None)
    num = random.randrange(min, max)
    if min < 0:
        msg = {
            'msg': 'Not Allowed. Please provide a min that is bigger than 0'
        }
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)
    else:
        data = {
            'random': num
        }
        return Response(data, status=status.HTTP_200_OK)
