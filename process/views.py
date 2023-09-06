from django.http import JsonResponse
from . import fn # use this for implementing any sanitizer functions
import requests

jsondata={}

#API function
def api(request):
    return JsonResponse(jsondata,safe=True)#change safe = True if the data is a dictionary

params = {
  'access_key': '30d8ca0fbba8daadbd4ff903c762fbc5',
  'query': 'Chennai'
}
api_result = requests.get('http://api.weatherstack.com/current', params)
jsondata = api_result.json()
#print(jsondata.keys()) to get the keys
# print(jsondata['current']) to get all the values available in current weather


#nandees forever
