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
    temp=json.loads(jsondata)
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
                "desc":""
                }
    
    for key, value in clean_data.items():
        try:
            clean_data[key] =float(value)
        except:
            clean_data[key] = 0
    clean_data["desc"],clean_data["icon"]=temp_desc(float(clean_data["tempout"]),float(clean_data["humidity"]),float(clean_data["dew"]),float(clean_data["rainrate"]),float(clean_data['windspeed']))
    return clean_data
