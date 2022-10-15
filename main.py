# import the necessary modules
import smtplib
import ssl
import csv
from email.message import EmailMessage

sender = ''  # add your sender email address
password = ''  # add your app password

# add the subject of the email you want to send
subject = 'Python Email Automation Script Test Pt. 2'
body_message = '''This script reads data from a CSV file (Excel), and sends an with the an email to all users defined in the CSV file with the attached subject and password'''  # type the message you want to send

# connect to our outgoing mail SMTP server
context = ssl.create_default_context()
server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)

server.login(sender, password)

# The formula we'll use to send emails
with open(r'', 'r') as csvfile: # Enter the path to your CSV file
    datareader = csv.reader(csvfile)
    for row in datareader:
        email = EmailMessage()
        email['From'] = sender
        email['To'] = row
        email['Subject'] = subject
        email.set_content(body_message)
        server.send_message(email)
        print(f"The message sent to {row} has been completed.")
        
# Close the server, terminate program
server.close()
print('Program has been terminated')
