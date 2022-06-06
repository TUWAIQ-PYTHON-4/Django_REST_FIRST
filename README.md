# Django_REST_FIRST

## Using Django REST Framework , create a new porject and develop those two API endpoints (urls)

### API path:  my_app/date  ['GET']
- This returns the current date for today.    
Example response :           
       { "date" : "Today is 2022-06-06 !" }
       
       
       
### API path : my_app/random ['POST']
- This api needs a min , max JSON object , and based on it, it will generate a random number between the minimum and maximum value . if the minimum value is less than 0 , then return a response that it is not supported. else return a the random number .     

Example Request JSON: 
     {"min" : 5, "max" : 200}
     
     
Example Response JSON:
       {"random" : 26}

Example Response if min number less than 0 (the status should be status.HTTP_400_BAD_REQUEST:
    {"msg", "Not Allowed. Please provide a min that is bigger than 0"}
    
