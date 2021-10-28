import pandas as pd
import smtplib as smtp
import datetime as dt


def send_email(to_email, body_msg):
    my_email = "Someoneanonymous475@gmail.com"
    password = "Sp1d#rweb"
    smtp_address = "smtp.gmail.com"

    with smtp.SMTP_SSL(smtp_address, 465) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:Happy Birthday!!!\n\n{body_msg}")


bd_info = pd.read_csv("birthday_data.csv")

now = dt.datetime.now()
today_day = now.day
today_month = now.month
today_year = now.year

for index, row in bd_info.iterrows():
    email = row['EMAIL']
    name = row["NAME"]
    month = row["MONTH"]
    day = row["DAY"]
    year = row["YEAR"]
    fam_or_friend = row["TYPE"]

    if today_month == month and today_day == day:
        if fam_or_friend == "Family":
            msg_path = "birthday_msg_family.txt"
        else:
            msg_path = "birthday_msg_friend.txt"

        with open(msg_path, "r") as msg:
            msg_contents = msg.read().replace("[Name]", name).replace("[years]", str(today_year - year))

        send_email(email, msg_contents)
