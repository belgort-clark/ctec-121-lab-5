# CTEC 121 - Clark College
# Sending Email with Python
# by Bruce Elgort
# August 20, 2017
# Lab No. 5

# Import the Simple Mail Transport Library
# https://docs.python.org/2/library/smtplib.html
import smtplib

def main():

    # Configure the SMTP host that will be used to send mail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    
    # send an 'ehlo' command to establish converstation
    server.ehlo()

    # Put the SMTP connection in TLS (Transport Layer Security) mode
    server.starttls()

    # Get some user inputs
    username = input("Enter your email address for GMail: ")
    print("WARNING: YOUR PASSWORD WILL BE DISPLAYED IN FULL VIEW AS YOU TYPE IT")
    password = input("enter your password for GMail: ")

    try:
        # Try and login to the mail server
        server.login(username, password)
        # Get text of mail message
        msg = input("Enter the text of the message to send: ")
        # Get recipient of email
        sendTo = input("Enter email address of person to send this message to: ")
        # Send the message
        server.sendmail(username, sendTo, msg)
        print("Email sent!")
    except:
        print("Hmmm.... something went wrong")
        print("Please paste this URL to your browser to learn more about")
        print("how to resolove.")
        print("https://support.google.com/mail/answer/78754 ")


main()
