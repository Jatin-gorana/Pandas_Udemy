from smtplib import SMTP
import datetime
import pandas as pd

Password = 'jnwmegaxoxekbhsu'
Sender = 'techtricks9816@gmail.com'

now = datetime.datetime.now()
actual_date = (now.day, now.month)

Emails_list = pd.read_excel('email_list.xlsx')

names = Emails_list['Name']
emails = Emails_list['Email']

# Connect to the server of the sender email account
connect_server = SMTP(host='smtp.gmail.com', port=587)

# Encrypt our email using this protocol
connect_server.starttls()

connect_server.login(Sender, Password)

for item in range(len(emails)):
    name = names[item]
    email = emails[item]

    # Send email to each recipient
    # subject = f"Hello {name}, Happy Birthday!"
    # message = f"Dear {name},\n\nWishing you a very happy birthday!\n\nBest regards,\nYour Name"
    # email_content = f"Subject: {subject}\n\n{message}"

    #Adjust the time of sending emails to customer using control flow if stmts
    if actual_date == (15, 7):
        message = f"Dear {name},\n\nWishing you a very happy anniversary!\n\nBest regards,\nYour Name"
        connect_server.sendmail(Sender, email, message)
    elif actual_date == (14,7):
        message = f"Dear {name},\n\nWishing you a happy raksha bandhan!\n\nBest regards,\nYour Name"
        connect_server.sendmail(Sender, email, message)


    # connect_server.sendmail(Sender, email, email_content)

    print(f"Email sent to {name} at {email}")

connect_server.quit()

# from smtplib import SMTP
# import datetime
# import pandas as pd
# # import pip
# # pip.main(["install", "openpyxl"])
#
# Password = '#j3killer'
# Sender = 'techtricks9816@gmail.com'
# now = datetime.datetime.now()
# actual_date = (now.day, now.month)
#
# Emails_list = pd.read_excel('email_list.xlsx')
#
# names = Emails_list['Name']
# emails = Emails_list['Email']
#
# connect_server = SMTP(host='smtp.gmail.com', port=587)
#
# connect_server.starttls()
#
# connect_server.login(Sender, Password)
#
# for item in range(len(emails)):
#     name = names[item]
#     email = emails[item]
#
# connect_server.close()