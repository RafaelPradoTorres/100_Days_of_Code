##################### Extra Hard Starting Project ######################
# can use python anywhere to automate it!!

import pandas as pd
import datetime as dt
from random import randint
import smtplib

# 1. Update the birthdays.csv
data = pd.read_csv("./birthdays.csv")
today = dt.datetime.today()

# 2. Check if today matches a birthday in the birthdays.csv
today = (today.month, today.day)


birthday_dict = {(data_row.month, data_row.day):data_row for (index, data_row) in data.iterrows()}
try:
    niver_de_hoje = birthday_dict[today]
except KeyError:
    print("Sem aniversários hoje, amigo!!!")
else:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
    # with the person's actual name from birthdays.csv
    file = f"./letter_templates/letter_{randint(1,3)}.txt"
    with open(file) as letter:
        content = letter.read()

        content = content.replace("[NAME]", niver_de_hoje["name"])


    my_email = "testerafa04@gmail.com"
    password = "bkhm ycpm uimz qnwz"



    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr = my_email,
                            to_addrs = niver_de_hoje["email"],
                            msg = f"Subject: Happy birthday!\n\n{content}")



# 4. Send the letter generated in step 3 to that person's email address.
