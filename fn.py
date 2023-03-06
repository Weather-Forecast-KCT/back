import datetime
import json
def farenheit_to_celcius(temp):
    return float("{:.1f}".format((float(temp)-32)*5/9))
def temp_desc(temperature, humidity, dew,rain_rate,wind_speed):
    now = datetime.datetime.now()
    def suff(icon):
        if int(now.strftime("%H"))>=6 and int(now.strftime("%H"))<18:
            return icon+"d"
        else:
            return icon+"n"
    #first we check rain rate
    if rain_rate > 0.2 and rain_rate < 2.5:
        return "shower rain",suff("09")
    elif rain_rate > 2.5:
        if wind_speed > 50:
            return "thunderstorm",suff("11")
        else:
            return "rain",suff("10")
    #then temperature
    elif temperature < 10:
        if humidity < 50:
            return "clear sky",suff("01")
        elif humidity < 80:
            return "few clouds",suff("02")
        else:
            return "mist",suff("50")
    elif temperature < 20:
        if humidity < 50:
            return "scattered clouds",suff("03")
        elif humidity < 80:
            return "broken clouds",suff("04")
        else:
            return "mist",suff("50")
    elif temperature < 30:
        if humidity < 50:
            return "clear sky",suff("01")
        elif humidity < 80:
            return "few clouds",suff("02")
        else:
            return "mist",suff("50")
    else:
        return "clear sky",suff("01")
def clean(jsondata):
    #temp=json.loads(jsondata)
    temp=dict(jsondata)
    
    clean_data={"tempin":farenheit_to_celcius(temp["tempin"]),
                "tempout":farenheit_to_celcius(temp["tempout"]),
                "humidity":temp["humout"],
                "windspeed":temp['windspd'],
                "winddir":temp["winddir"],
                "rainrate":temp["rainr"],
                "dew":temp["dew"],
                "uv":temp["uv"],
                "heat":temp["heat"],
                "icon":"",
                "desc":"",
                 }
    
    for key, value in clean_data.items():
        try:
            clean_data[key] =float(value)
        except:
            clean_data[key] = 0
    clean_data["desc"],clean_data["icon"]=temp_desc(float(clean_data["tempout"]),float(clean_data["humidity"]),float(clean_data["dew"]),float(clean_data["rainrate"]),float(clean_data['windspeed']))
    #temporary data for chart
    
    return clean_data

def chart60(past1min):
    temp={"60sec": [        
        {"id": 1},       
        {"id": 2},
        {"id": 3},
        {"id": 4},
        {"id": 5},
        {"id": 6},
        {"id": 7},
        {"id": 8},
        {"id": 9},
        {"id": 10},
        {"id": 11},
        {"id": 12},
        {"id": 13},
        {"id": 14},
        {"id": 15},
        {"id": 16},
        {"id": 17},
        {"id": 18},
        {"id": 19},
        {"id": 20},
        {"id": 21},
        {"id": 22},
        {"id": 23},
        {"id": 24},
        {"id": 25},
        {"id": 26},
        {"id": 27},
        {"id": 28},
        {"id": 29},
        {"id": 30},
        {"id": 31},
        {"id": 32},
        {"id": 33},
        {"id": 34},
        {"id": 35},
        {"id": 36},
        {"id": 37},
        {"id": 38},
        {"id": 39},
        {"id": 40},
        {"id": 41},
        {"id": 42},
        {"id": 43},
        {"id": 44},
        {"id": 45},
        {"id": 46},
        {"id": 47},
        {"id": 48},
        {"id": 49},
        {"id": 50},
        {"id": 51},
        {"id": 52},
        {"id": 53},
        {"id": 54},
        {"id": 55},
        {"id": 56},
        {"id": 57},
        {"id": 58},
        {"id": 59},
        {"id": 60},    
        ]}
    
    for i, j in enumerate(past1min.values()):
        temp["60sec"][i]["temperature"] = j["tempout"]
        temp["60sec"][i]["humidity"] = j["humidity"]
        temp["60sec"][i]["windSpeed"] = j["windspeed"]
    
    return temp