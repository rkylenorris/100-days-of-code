# import smtplib as smtp
#
# my_email = "someoneanonymous475@gmail.com"
#
# with smtp.SMTP_SSL("smtp.gmail.com", 465) as connection:
#     connection.login(user=my_email, password="Sp1d#rweb")
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="rodermus@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of the email")


import datetime as dt

now = dt.datetime.now()
year = now.year
print(now.weekday())

date_of_birth = dt.datetime(year=1991, month=2, day=26, hour=17, minute=30)
print(date_of_birth)
