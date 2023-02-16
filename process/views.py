import paho.mqtt.client as mqtt
import json
from django.http import JsonResponse 
from colorama import Fore, Style # for good experience in command line
import datetime
jsondata={}
def clean(jsondata):
    temp=json.loads(jsondata)
    clean_data={"tempin":temp["tempin"],
                "tempout":temp["tempout"],
                "humidity":temp["humout"],
                "windspeed":temp['windspd'],
                "winddir":temp["winddir"],
                "rainrate":temp["rainr"],
                "dew":temp["dew"],
                "uv":temp["uv"],
                "icon":"11d"
                }
    return clean_data
#API function
def api(request):
    return JsonResponse(clean(jsondata),safe=True)#change safe = True if the data is a dictionary
#call this function whenever the message is recieved
def on_message(client, userdata,message):
    global jsondata
    jsondata =message.payload
    jsondata=jsondata.decode('utf-8')
    now = datetime.datetime.now()
    print(Fore.GREEN+"Got a message in the topic : "+message.topic+" at"+now.strftime(" %H:%M:%S")+Style.RESET_ALL)
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