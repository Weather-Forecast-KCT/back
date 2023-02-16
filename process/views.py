import paho.mqtt.client as mqtt
import json
from django.http import JsonResponse , HttpResponse
from colorama import Fore, Style # for good experience in command line
unfiltered_data={}
def jsontodict(unfiltered_data):
    unfiltered_data = json.loads(unfiltered_data)
    return unfiltered_data
#call this function for sending realtime data
def to_react(request):
    return JsonResponse(jsontodict(unfiltered_data),safe=True)#change safe = True if the data is a dictionary
#call this function whenever the message is recieved
def on_message(client, userdata,message):
    global unfiltered_data
    unfiltered_data =message.payload
    unfiltered_data=unfiltered_data.decode('utf-8')
    #filter the unfiltered data and connect to databases in v0.1.1
    #filtered_data = unfiltered_data - useless
    print(Fore.GREEN+"Got a message in the topic : "+message.topic+Style.RESET_ALL)
    #print(Fore.YELLOW+unfiltered_data+Style.RESET_ALL)
    

#this part Subscribes to the MQTT Broker . This happens only one time one the first boot . If it can't connect to mqtt it will show error on console
try:
    #mosquitto_sub -h 192.168.29.79 -v -t weatherwflexp.json -p 1884 -u clan4 -P clan4 > data.txt
    client = mqtt.Client()
    #client.on_message = on_message
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