import paho.mqtt.client as mqtt
from django.http import JsonResponse 
from colorama import Fore, Style # for good experience in command line
import datetime
from . import fn
from collections import defaultdict
import time
jsondata={}


#API function
def api(request):
    return JsonResponse(fn.clean(jsondata),safe=True)#change safe = True if the data is a dictionary
#call this function whenever the message is recieved
def on_message(client, userdata,message):
    global jsondata
    jsondata =message.payload
    jsondata=jsondata.decode('utf-8')
    now = datetime.datetime.now()
    print(Fore.GREEN+"Got a message in the topic : "+message.topic+" at"+now.strftime(" %H:%M:%S")+Style.RESET_ALL)
    #print(Fore.YELLOW+str(fn.clean(jsondata))+Style.RESET_ALL)
    #print(Fore.YELLOW+unfiltered_data+Style.RESET_ALL)
    

#this part Subscribes to the MQTT Broker . This happens only one time one the first boot . If it can't connect to mqtt it will show error on console
try:
    #mosquitto_sub -h 192.168.29.79 -v -t weatherwflexp.json -p 1884 -u clan4 -P clan4 > data.txt
    client = mqtt.Client()
    client.username_pw_set("clan4", "clan4")
    client.connect("192.168.29.79", 1884, 10)
    client.subscribe("weatherwflexp.json", 0)
    print(Fore.GREEN+"Successfully subscribed to MQTT server"+Style.RESET_ALL)
    client.loop_start()
    client.on_message = on_message
   
    
    
except:
    print(Fore.RED+"Error connecting to MQTT Broker")
    print("Please check the MQTT Broker and try again"+Style.RESET_ALL)
    exit()

#store past 5 second values of fn.clean(jsondata) and an api to send it
import time

past5sec = {}

def live_data(request):
    global past5sec
    
    # Get the cleaned JSON data
    cleaned_data = fn.clean(jsondata)
    
    # Add the cleaned data to the past5sec dict for each keyword
    for keyword, value in cleaned_data.items():
        past5sec.setdefault(keyword, [])
        past5sec[keyword].append({'id': len(past5sec[keyword]) + 1, 'value': value})
        if len(past5sec[keyword]) > 5:
            past5sec[keyword].pop(0)
    
    # Update the ID values in the past5sec dict to represent seconds ago
    for keyword, values in past5sec.items():
        for i in range(len(values)):
            values[i]['id'] = len(values) - i
    
    # Convert the past5sec dict to a nested data JSON response
    response_data = {}
    for keyword, values in past5sec.items():
        response_data[keyword] = values
    
    # Return the JSON response
    return JsonResponse(response_data, safe=False)
