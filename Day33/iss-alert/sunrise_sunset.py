import requests
import datetime as dt
import pytz

MY_LAT = 33.027859
MY_LONG = -80.156120


class NightTime:

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    def __init__(self):
        self.response = requests.get(
            url="https://api.sunrise-sunset.org/json",
            params=self.parameters
        )
        self.response.raise_for_status()
        self.data = self.response.json()

    def is_nighttime(self, time_now):
        sunrise_str = self.data["results"]["sunrise"].split("+")[0].replace("T", " ")
        sunset_str = self.data["results"]["sunset"].split("+")[0].replace("T", " ")
        sunrise_dt = dt.datetime.strptime(sunrise_str, "%Y-%m-%d %H:%M:%S")
        sunset_dt = dt.datetime.strptime(sunset_str, "%Y-%m-%d %H:%M:%S")
        local_timezone = pytz.timezone("US/Eastern")
        local_sunrise_dt = sunrise_dt.astimezone(local_timezone)
        local_sunset_dt = sunset_dt.astimezone(local_timezone)
        local_sunrise_offset = local_sunrise_dt.strftime('%z')
        local_sunset_offset = local_sunset_dt.strftime('%z')
        sunrise_time_offset = int(local_sunrise_offset) // 100
        sunset_time_offset = int(local_sunset_offset) // 100
        sunrise_dt = sunrise_dt + dt.timedelta(hours=sunrise_time_offset)
        sunset_dt = sunset_dt + dt.timedelta(hours=sunset_time_offset)
        if time_now > sunset_dt and time_now < sunrise_dt:
            return True
        else:
            return False
