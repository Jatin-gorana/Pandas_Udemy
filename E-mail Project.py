from smtplib import SMTP

sender = 'techtricks9816@gmail.com'
password = 'ufqytqfsuutiwulm'
recipient = 'jatingorana123@gmail.com'

# Connect to the SMTP server
smtp_server = SMTP(host='smtp.gmail.com', port=587)
smtp_server.starttls()

# Login to your Gmail account
smtp_server.login(user=sender, password=password)

# Send the email
message = 'Subject: Test Email\n\nHi, there!!'
smtp_server.sendmail(from_addr=sender, to_addrs=recipient, msg=message)

# Close the connection
smtp_server.quit()




# from smtplib import SMTP
# sender = 'techtricks9816@gmail.com'
# Password = '#j3killer'
# recipient = 'jatingorana123@gmail.com'
# connect_server = SMTP( host = 'smtp.serveraddress.com', port = 587)
# connect_server
# connect_server.starttls()
# connect_server.login(user= sender, password=Password)
# connect_server.sendmail(from_addr=sender, to_addrs=recipient, msg='Hi, there!!')
# connect_server.close()