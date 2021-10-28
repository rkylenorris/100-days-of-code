import smtplib as smtp
import datetime as dt
from random import choice

with open("quotes.txt") as data:
    lines = data.readlines()


def send_email(msg):
    my_email = "someoneanonymous475@gmail.com"

    with smtp.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=my_email, password="Sp1d#rweb")
        connection.sendmail(
            from_addr=my_email,
            to_addrs="rodermus@yahoo.com",
            msg=f"Subject:Inspirational Quote\n\n{msg}")


now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 6: # indexes at zero stating on monday so 6 is sunday
    quote = choice(lines)
    send_email(quote)
else:
    print("Today is not the day to send the email")
