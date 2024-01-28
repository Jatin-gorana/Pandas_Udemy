from smtplib import SMTP

sender = 'techtr9816@gmail.com'   #your own email and password
password = 'ufqytqftiwulm'
recipient = 'jatin@gmail.com'  #recievers email address

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
# sender = 'tech@gmail.com'
# Password = 'yourpassword'
# recipient = 'jatin@gmail.com'
# connect_server = SMTP( host = 'smtp.serveraddress.com', port = 587)
# connect_server
# connect_server.starttls()
# connect_server.login(user= sender, password=Password)
# connect_server.sendmail(from_addr=sender, to_addrs=recipient, msg='Hi, there!!')
# connect_server.close()
