##################### Extra Hard Starting Project ######################
# The personal data such as email and passwords are changed/removed
import datetime
import random
import smtplib
import pandas

EMAIL = ""
PASSWORD = ""


def send_wish(name, email_to):
    letter_number = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_number}.txt") as letter_file:
        message = letter_file.read()
        message = message.replace("[NAME]", name)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=email_to,
                            msg=f"Subject:Happy Birthday\n\n{message}")


today = datetime.datetime.now()
day = today.day
month = today.month

birthday_data = pandas.read_csv("birthdays.csv")
for index, row in birthday_data.iterrows():
    row_list = row.to_list()
    name = row_list[0]
    email = row_list[1]
    birthday_month = row_list[3]
    birthday_day = row_list[4]

    if birthday_day == day and birthday_month == month:
        send_wish(name, email)




