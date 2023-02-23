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
    jsondata={"stnname":"Sample","stnmod":17,"ver":4.37,"mac":"8C:4B:14:DA:26:9C","apmac":"8C:4B:14:DA:26:9D","ip":"192.168.29.135","ssid":"test","rssi":-56,"wifimod":0,"lastboot":1676270816,"uptime":1264,"wflver":"2.41","loctime":1676291871,"utctime":1676272071,"tzone":34,"units":41,"conlati":110,"conlongi":-769,"wfllati":-300.0000000,"wfllongi":-300.0000000,"tempout":"88.1","humout":"24","tempin":"86.2","humin":"26","windspd":"18.0","winddir":"219","windavg2":"9.8","windavg10":"8.2","gust":"17.0","gustdir":"225","bar":"28.847","bartr":"20","dew":"47","cdew":"46.8","chill":"88","heat":"86","thsw":"---","uv":"---","solar":"---","rainr":"0.00000","storm":"0.00000","rain15":"0.00000","rain1h":"0.00000","raind":"0.00000","rain24":"0.00000","rainmon":"0.00000","rainyear":"1.12598","etday":"0.000","etmon":"0.00","etyear":"0.00","xt":["---","---","---","---","---","---","---"],"xlt":["---","---","---","---"],"xst":["---","---","---","---"],"xh":["---","---","---","---","---","---","---"],"xsm":["---","---","---","---"],"xlw":["---","---","---","0"],"bat":"4.80","trbat":"0","foreico":"0","forrule":"---","sunrt":"16:59","sunst":"4:45","hlbar":["28.844","28.858","12:33","12:14","28.989","28.810","28.989","28.810"],"hlwind":["---","17.0","---","12:23","17.0","---","17.0","---"],"hltempin":["85.4","85.8","12:24","12:35","85.8","81.0","85.8","81.0"],"hlhumin":["26","29","12:26","12:34","63","26","63","26"],"hltempout":["87.9","88.9","12:14","12:22","88.9","68.7","88.9","68.7"],"hlhumout":["24","26","12:23","12:15","89","24","89","24"],"hldew":["47","50","12:23","12:20","68","47","68","47"],"hlchil":["87","---","12:16","---","---","69","---","83"],"hlheat":["---","86","---","12:15","88","---","86","---"],"hlthsw":["---","---","---","9:56"," 0","---","4368","---"],"hlsolar":["---","0","---","179:21","0","---","0","---"],"hluv":["---","0.0","---","0:00","0.0","---","0.0","---"],"hlrainr":["0.000","0.000","---","---","0.000","---","2.984","---"],"hlxt0":["---","---","---","---","---","---","---","---"],"hlxt1":["---","---","---","---","---","---","---","---"],"hlxt2":["---","---","---","---","---","---","---","---"],"hlxt3":["---","---","---","---","---","---","---","---"],"hlxt4":["---","---","---","---","---","---","---","---"],"hlxt5":["---","---","---","---","---","---","---","---"],"hlxt6":["---","---","---","---","---","---","---","---"],"hlxh0":["---","---","---","---","---","---","---","---"],"hlxh1":["---","---","---","---","---","---","---","---"],"hlxh2":["---","---","---","---","---","---","---","---"],"hlxh3":["---","---","---","---","---","---","---","---"],"hlxh4":["---","---","---","---","---","---","---","---"],"hlxh5":["---","---","---","---","---","---","---","---"],"hlxh6":["---","---","---","---","---","---","---","---"],"hlxst0":["---","---","---","---","---","---","---","---"],"hlxst1":["---","---","---","---","---","---","---","---"],"hlxst2":["---","---","---","---","---","---","---","---"],"hlxst3":["---","---","---","---","---","---","---","---"],"hlxlt0":["---","---","---","---","---","---","---","---"],"hlxlt1":["---","---","---","---","---","---","---","---"],"hlxlt2":["---","---","---","---","---","---","---","---"],"hlxlt3":["---","---","---","---","---","---","---","---"],"hlxsm0":["---","---","---","---","---","---","---","---"],"hlxsm1":["---","---","---","---","---","---","---","---"],"hlxsm2":["---","---","---","---","---","---","---","---"],"hlxsm3":["---","---","---","---","---","---","---","---"],"hlxlw0":["---","---","---","---","---","---","---","---"],"hlxlw1":["---","---","---","---","---","---","---","---"],"hlxlw2":["---","---","---","---","---","---","---","---"],"hlxlw3":["---","---","---","---","---","---","---","---"]}

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
    #exit()

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
