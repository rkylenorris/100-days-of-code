import requests
import datetime as dt
import pytz

MY_LAT = 33.027859
MY_LONG = -80.156120

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise_str = data["results"]["sunrise"].split("+")[0].replace("T", " ")
sunset_str = data["results"]["sunset"].split("+")[0].replace("T", " ")
sunrise_dt = dt.datetime.strptime(sunrise_str, "%Y-%m-%d %H:%M:%S")
sunset_dt = dt.datetime.strptime(sunset_str, "%Y-%m-%d %H:%M:%S")
local_timezone = pytz.timezone("US/Eastern")
utc_sunrise = sunrise_dt.replace(tzinfo=pytz.utc)
utc_sunset = sunset_dt.replace(tzinfo=pytz.utc)
local_sunrise_dt = sunrise_dt.astimezone(local_timezone)
local_sunset_dt = sunset_dt.astimezone(local_timezone)
local_sunrise_offset = local_sunrise_dt.strftime('%z')
local_sunset_offset = local_sunset_dt.strftime('%z')
sunrise_time_offset = int(local_sunrise_offset) // 100
sunset_time_offset = int(local_sunset_offset) // 100
sunrise_dt = sunrise_dt + dt.timedelta(hours=sunrise_time_offset)
sunset_dt = sunset_dt + dt.timedelta(hours=sunset_time_offset)


