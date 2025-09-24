import smtplib, datetime as dt
from random import choice

my_email = "testerafa04@gmail.com"
password = "bkhm ycpm uimz qnwz"

# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls() #secure the connection
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="rafateste04@outlook.com", msg="Subject:OMG!! Hiii!\n\nHi, fella!!")
# connection.close()
day_of_week = dt.datetime.now().weekday()
if day_of_week == 1:
    with open('./quotes.txt', 'r') as quote_file:
        quotes = quote_file.readlines()
        message = choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls() #secure the connection
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="rafateste04@outlook.com", msg=f"Subject:Vamos, Rafa!\n\n{message}")

# import datetime as dt
#
# now = dt.datetime.now() #datetime object
# year = now.year #int
# month = now.month
# day_of_week = now.weekday()
#
# date_of_birth = dt.datetime(year=2004, month=12, day=29, hour=18)
# print(date_of_birth)