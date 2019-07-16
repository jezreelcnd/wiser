from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings

from .models import Posts

import json
import requests

# Create your views here.

def index(request):
  #return HttpResponse('HELLO FROM POSTS')
  # return render(request, 'profile_admin/index.html', {
  #     'title':'Hello'
  #})

  posts = Posts.objects.all()[:10]

  context = {
    'title': 'Latest Posts',
    'posts': posts
  }

  return render(request, 'profile_admin/index.html', context)

def details(request, id):
  post = Posts.objects.get(id=id)

  context = {
    'post': post
  }

  return render(request, 'profile_admin/details.html', context)



@api_view(["POST"])
def IdealWeight(request):
    try:
        ##height=json.loads(heightdata.body)
        #weight=str(height*10)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print (body)
        weight = body['weight']
        if weight is None:
          return JsonResponse("weight key not found in request payload")
        else:
          return JsonResponse("Ideal weight should be: "+str(weight)+" kg",safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def AsociateUser(request):
    try:
        # defining the api-endpoint  
        API_ENDPOINT = "https://www.linkedin.com/uas/oauth2/accessToken"
        API_ENDPOINT_DATA ="https://api.linkedin.com/v2/clientAwareMemberHandles?q=members&projection=(elements*(primary,type,handle~))"
        # your API key here 
        API_KEY = "86m13p23ezn5bi"
        API_SECRET = "nsGe8KIyHdf46EbD"
        REDIRECT_URL= "http://localhost:3000/signinlinkedin"
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print (body)
        code = body['code']
        print ("access code: "+code)
        if code is None:
          return JsonResponse("code key not found in request payload")
        else:
          #return JsonResponse("code: "+str(code)+" kg",safe=False)
          # data to be sent to api 
          data = {'grant_type': 'authorization_code', 
                  'redirect_uri': REDIRECT_URL, 
                  'client_id': API_KEY, 
                  'client_secret': API_SECRET,
                  'code':code} 
  
          # sending post request and saving response as response object 
          r = requests.post(url = API_ENDPOINT, data = data) 
  
          # extracting response text  
          response_json = r.text 
          print("Text in URL is:%s"%response_json)
          body_at = json.loads(response_json)
          print (body_at)
          result = response_json.find('access_token') 
          print ("Substring 'access_token' found at index:", result ) 
          if (int(result) > 0 ):
            access_token = body_at['access_token']
            print ("access token: "+access_token)
            data = {'oauth2_access_token': access_token,
                    'format': 'json'} 
            # sending post request and saving response as response object 
            response_json  = requests.get(url = API_ENDPOINT_DATA, data = data) 
            print(response_json.text)
            # Uncomment when linkedin API works
            jsonResponse = json.dumps({'emailAdress': 'jezreel@gmail.com'})
            return JsonResponse(jsonResponse,safe=False)
          else:
            error = body_at['error']
            return JsonResponse("error: "+str(error),safe=False) 

    except ValueError as e:
        print ("Error: "+e)
        return HttpResponse(status=404)