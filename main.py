import smtplib
import datetime as dt
import random
import pandas

TEST_EMAIL = "test@outlook.com"
TEST_PASSWORD = "test"

now = dt.datetime.now()
today = (now.month, now.day)

bday_df = pandas.read_csv("birthdays.csv")
bday_dict = {(row.month, row.day): row for (index, row) in bday_df.iterrows()}

if today in bday_dict:
  bday_person = bday_dict[today]
  num = random.randint(1, 3)
  file_path = f"letter_templates/letter_{num}.txt"
  with open(file_path) as letter_file:
    contents = letter_file.read()
    contents = contents.replace("[NAME]", bday_person["name"])

  with smtplib.SMTP("smtp.office365.com")as connection:
      connection.starttls()
      connection.login(user=TEST_EMAIL, password=TEST_PASSWORD)
      connection.sendmail(
          from_addr=TEST_EMAIL,
          to_addrs=bday_person["email"],
          msg=f"Subject:Happy Birthday!\n\n{contents}")