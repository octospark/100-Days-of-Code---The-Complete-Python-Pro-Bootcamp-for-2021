import datetime
import smtplib
import random
# Provide the email and password

def send_motivational_quote(message):
    email = ""
    password = ""

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(from_addr=email,
                            to_addrs="mail@gmail.com",
                            msg=f"Subject:Quote of the Day\n\n{message}")


with open("quotes.txt", 'r') as file:
    quote = random.choice(file.readlines())

now = datetime.datetime.now()
today = now.weekday()


if today == 3:
    send_motivational_quote(quote)
