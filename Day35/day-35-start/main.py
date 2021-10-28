import requests

parameters = {
    "lat": 33.027859,
    "lon": -80.156120,
    "appid": "833d1b27347f31f4487f71973b11092e"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
print(response.json())
