import smtplib
import random
import datetime as dt 
import pandas as pd

letters = []

df = pd.read_csv("./src/birthdays.csv")
birthdays = df.to_dict(orient="records")
now = dt.datetime.now()
day_of_week = now.weekday()
my_email = "email"
password = "password"

with open("./src/letter_templates/letter_1.txt") as letter_1:
    letter1 = letter_1.readlines()
    letters.append(letter1)

with open("./src/letter_templates/letter_2.txt") as letter_2:
    letter2 = letter_2.readlines()
    letters.append(letter2)

with open("./src/letter_templates/letter_3.txt") as letter_3:
    letter3 = letter_3.readlines()
    letters.append(letter3)

random_letter = random.choice(letters)

for dictionary in birthdays:
    if dictionary["month"] == now.month and dictionary["day"] == now.day:
        name = dictionary["name"]
        letter_email = dictionary["email"]
        letter_string = "".join(random_letter)
        new_string = letter_string.replace("[NAME]", name)
        random_letter.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=letter_email,
                msg=f"Subject:Happy Birthday\n\n{new_string}"
            )



