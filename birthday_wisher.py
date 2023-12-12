import pandas
import datetime as dt
import smtplib

birthdate = pandas.read_csv("birthdates.csv")
# print(birthdate)
birthdates_dictionary = {}
i = 0
for row in birthdate.iterrows():
    new_list = [birthdate.email[i], birthdate.month[i], birthdate.year[i], birthdate.day[i], birthdate.name[i]]
    # print(new_list)
    birthdates_dictionary[i] = new_list
    i = i + 1

# print(birthdates_dictionary)

# Getting the current date
current_date = dt.datetime.now()
current_day_in_english = current_date.strftime("%A")
current_month = current_date.month
current_day_of_month = current_date.day

for value in birthdates_dictionary.values():
    if current_day_of_month and current_month in value:
        # print("Present")
        email_address = "morkasebrahim3@gmail.com"
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(email_address, "alhd fcpw miau jyxb")
        connection.sendmail(from_addr=email_address,
                            to_addrs=f"{value[0]}",
                            msg=f"Subject: Birthday Wish\n\n Happy birthday {value[4]}")
        connection.close()