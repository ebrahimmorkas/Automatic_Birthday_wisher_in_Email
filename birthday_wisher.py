import pandas
import datetime as dt
import smtplib

birthdate = pandas.read_csv("birthdates.csv")
# print(birthdate)
birthdates_dictionary = {}
i = 0
for row in birthdate.iterrows():
    new_list = [birthdate.email[i], birthdate.month[i], birthdate.year[i], birthdate.day[i]]
    # print(new_list)
    birthdates_dictionary[birthdate.name[i]] = new_list
    i = i + 1

# print(birthdates_dictionary)

# Getting the current date
current_date = dt.datetime.now()
current_day_in_english = current_date.strftime("%A")
current_month = current_date.month
