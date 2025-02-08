##################### Normal Starting Project ######################

import datetime as dt
import smtplib
import pandas
import random

my_email = "k.andrzejewski225@gmail.com"
password = "qqrcaucqtjmzrjvh"

now = dt.datetime.now()
today_day = now.day
today_month = now.month
today = (today_month, today_day)

birthday_file = pandas.read_csv("birthdays.csv")

birthday_dict = {(row['month'], row['day']): row for index, row in birthday_file.iterrows()}

if today in birthday_dict:
    number = random.randint(1,3)
    random_letter = f"letter_{number}.txt"
    birthday_person = birthday_dict[today]
    with open(random_letter, 'r') as letter:
        current_letter=letter.read()
        birthday_letter = current_letter.replace("[NAME]", birthday_person["name"])
        # print(birthday_letter)

    dir_address = birthday_dict[today]["email"]

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=dir_address, msg=f"Subject: HAPPY BIRTHDAY!\n\n{birthday_letter}")








