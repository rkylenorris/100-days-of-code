import requests
import sunrise_sunset as ss
import datetime as dt
import time
import smtplib as smtp


def send_email(to_email="Rodermus@gmail.com", body_msg="ISS is overhead at home!"):
    my_email = "Someoneanonymous475@gmail.com"
    password = "Sp1d#rweb"
    smtp_address = "smtp.gmail.com"

    with smtp.SMTP_SSL(smtp_address, 465) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:ISS In The Sky!!!\n\n{body_msg}")


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
position = response.json()["iss_position"]
lng = float(position["longitude"])
lat = float(position["latitude"])

nighttime = ss.NightTime()

while nighttime.is_nighttime(dt.datetime.now()):
    time.sleep(30)

if ss.MY_LAT == lat and ss.MY_LONG == lng:
    send_email()
