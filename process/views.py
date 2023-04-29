import paho.mqtt.client as mqtt
from django.http import JsonResponse , HttpResponse
from django.shortcuts import render
from colorama import Fore, Style # for good experience in command line
import datetime
from . import fn
from collections import defaultdict

import time
import csv,os
import threading
import json
jsondata={}
jsondata={"stnname":"Sample","stnmod":17,"ver":4.37,"mac":"8C:4B:14:DA:26:9C","apmac":"8C:4B:14:DA:26:9D","ip":"192.168.29.135","ssid":"test","rssi":-56,"wifimod":0,"lastboot":1676270816,"uptime":1264,"wflver":"2.41","loctime":1676291871,"utctime":1676272071,"tzone":34,"units":41,"conlati":110,"conlongi":-769,"wfllati":-300.0000000,"wfllongi":-300.0000000,"tempout":"88.1","humout":"24","tempin":"86.2","humin":"26","windspd":"18.0","winddir":"219","windavg2":"9.8","windavg10":"8.2","gust":"17.0","gustdir":"225","bar":"28.847","bartr":"20","dew":"47","cdew":"46.8","chill":"88","heat":"86","thsw":"---","uv":"---","solar":"---","rainr":"0.00000","storm":"0.00000","rain15":"0.00000","rain1h":"0.00000","raind":"0.00000","rain24":"0.00000","rainmon":"0.00000","rainyear":"1.12598","etday":"0.000","etmon":"0.00","etyear":"0.00","xt":["---","---","---","---","---","---","---"],"xlt":["---","---","---","---"],"xst":["---","---","---","---"],"xh":["---","---","---","---","---","---","---"],"xsm":["---","---","---","---"],"xlw":["---","---","---","0"],"bat":"4.80","trbat":"0","foreico":"0","forrule":"---","sunrt":"16:59","sunst":"4:45","hlbar":["28.844","28.858","12:33","12:14","28.989","28.810","28.989","28.810"],"hlwind":["---","17.0","---","12:23","17.0","---","17.0","---"],"hltempin":["85.4","85.8","12:24","12:35","85.8","81.0","85.8","81.0"],"hlhumin":["26","29","12:26","12:34","63","26","63","26"],"hltempout":["87.9","88.9","12:14","12:22","88.9","68.7","88.9","68.7"],"hlhumout":["24","26","12:23","12:15","89","24","89","24"],"hldew":["47","50","12:23","12:20","68","47","68","47"],"hlchil":["87","---","12:16","---","---","69","---","83"],"hlheat":["---","86","---","12:15","88","---","86","---"],"hlthsw":["---","---","---","9:56"," 0","---","4368","---"],"hlsolar":["---","0","---","179:21","0","---","0","---"],"hluv":["---","0.0","---","0:00","0.0","---","0.0","---"],"hlrainr":["0.000","0.000","---","---","0.000","---","2.984","---"],"hlxt0":["---","---","---","---","---","---","---","---"],"hlxt1":["---","---","---","---","---","---","---","---"],"hlxt2":["---","---","---","---","---","---","---","---"],"hlxt3":["---","---","---","---","---","---","---","---"],"hlxt4":["---","---","---","---","---","---","---","---"],"hlxt5":["---","---","---","---","---","---","---","---"],"hlxt6":["---","---","---","---","---","---","---","---"],"hlxh0":["---","---","---","---","---","---","---","---"],"hlxh1":["---","---","---","---","---","---","---","---"],"hlxh2":["---","---","---","---","---","---","---","---"],"hlxh3":["---","---","---","---","---","---","---","---"],"hlxh4":["---","---","---","---","---","---","---","---"],"hlxh5":["---","---","---","---","---","---","---","---"],"hlxh6":["---","---","---","---","---","---","---","---"],"hlxst0":["---","---","---","---","---","---","---","---"],"hlxst1":["---","---","---","---","---","---","---","---"],"hlxst2":["---","---","---","---","---","---","---","---"],"hlxst3":["---","---","---","---","---","---","---","---"],"hlxlt0":["---","---","---","---","---","---","---","---"],"hlxlt1":["---","---","---","---","---","---","---","---"],"hlxlt2":["---","---","---","---","---","---","---","---"],"hlxlt3":["---","---","---","---","---","---","---","---"],"hlxsm0":["---","---","---","---","---","---","---","---"],"hlxsm1":["---","---","---","---","---","---","---","---"],"hlxsm2":["---","---","---","---","---","---","---","---"],"hlxsm3":["---","---","---","---","---","---","---","---"],"hlxlw0":["---","---","---","---","---","---","---","---"],"hlxlw1":["---","---","---","---","---","---","---","---"],"hlxlw2":["---","---","---","---","---","---","---","---"],"hlxlw3":["---","---","---","---","---","---","---","---"]}
past1min = {}

#API function
def api(request):
    jsondata={"tempin": 25.0, "tempout": 29.0, "humidity": 62, "windspeed": 9, "winddir": 50, "rainrate": 0.0, "dew": 0, "uv": 0, "heat": 0, "icon": "01n", "desc": "clear sky"}
    return JsonResponse(jsondata,safe=True)#change safe = True if the data is a dictionary

#live data function
def live(request):
    return JsonResponse(fn.chart60(past1min))

#a def to save tempin value of jsondata 4 times a day in a csv file
'''def store():
    global jsondata
    now = datetime.datetime.now()
    filename = now.strftime("%d-%m-%Y") + ".csv"
    if not os.path.isfile(filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            temp=["Time","tempin", "tempout", "humidity", "windspeed", "winddir", "rainrate", "dew", "uv", "heat", "icon", "desc"]
            writer.writerow(temp)
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([now.strftime("%H:%M:%S")] + list(fn.clean(jsondata).values()))
    print(Fore.GREEN+"Saved tempin value at "+now.strftime("%d/%m/%Y %H:%M:%S")+Style.RESET_ALL)
    threading.Timer(60, store).start()'''



#this function is called whenever a message is recieved from the MQTT broker
def on_message(client, userdata,message):
    global jsondata
    global past1min
    jsondata =message.payload
    jsondata=jsondata.decode('utf-8')
    jsondata=json.loads(jsondata)
    now = datetime.datetime.now()
    print(Fore.GREEN+"Got a message in the topic : "+message.topic+" at"+now.strftime(" %H:%M:%S")+Style.RESET_ALL)
    #write currect clean json in a data.json so that we can use it in manage.py to store data in date.csv
    with open("data.json", "w") as f:
        json.dump((fn.clean(jsondata)), f, indent=4)
    #print(Fore.YELLOW+str(fn.clean(jsondata))+Style.RESET_ALL)
    #print(Fore.YELLOW+unfiltered_data+Style.RESET_ALL)
    '''past1min[time.time()] = fn.clean(jsondata)
    if len(past1min)>60:
        del past1min[min(past1min.keys())]'''
    

#store()
#this part Subscribes to the MQTT Broker . This happens only one time one the first boot . If it can't connect to mqtt it will show error on console
try:
    #mosquitto_sub -h <i.p> -v -t weatherwflexp.json -p 1884 -u clan4 -P clan4 > data.txt
    client = mqtt.Client()
    #client.username_pw_set("clan4", "clan4")
    client.connect("broker.hivemq.com", 1883, 10)
    client.subscribe("weatherwflexp.json", 0)
    client.enable_logger()
    print(Fore.GREEN+"Successfully subscribed to MQTT server"+Style.RESET_ALL)
    client.loop_start()
    client.on_message = on_message

except:
    print(Fore.RED+"Error connecting to MQTT Broker")
    print("Please check the MQTT Broker and try again"+Style.RESET_ALL)
    #exit()

#chuma 

def dailychart(request):
    chartdata={"chart": [
    {"id": 1, "day": "Monday", "temperature": 32, "humidity": 31, "windSpeed": 33}, 
    {"id": 2, "day": "Tuesday", "temperature": 30, "humidity": 29, "windSpeed": 31}, 
    {"id": 3, "day": "Wednesday", "temperature": 31, "humidity": 30, "windSpeed": 32}, 
    {"id": 4, "day": "Thursday", "temperature": 29, "humidity": 28, "windSpeed": 30}, 
    {"id": 5, "day": "Friday", "temperature": 30, "humidity": 29, "windSpeed": 31}
    ]}
    return JsonResponse(chartdata,safe=True)#change safe = True if the data is a dictionary
    
#nandees forever
