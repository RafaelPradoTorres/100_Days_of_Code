import smtplib

my_email = "testerafa04@gmail.com"
password = "bkhm ycpm uimz qnwz"

# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls() #secure the connection
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="rafateste04@outlook.com", msg="Subject:OMG!! Hiii!\n\nHi, fella!!")
# connection.close()

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls() #secure the connection
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="rafateste04@outlook.com", msg="Subject:OMG!! Hiii!\n\nHi, fella!!")

