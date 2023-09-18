import smtplib
from smtp_secret import password
passwd = password
emails = ["list","of","addressess"]
for email in emails:
    sender_email = "<replace with sender_email address"
    receiver_email = email
    message = f"""Subject: Example
      
    Body text to {email} goes here. 
    """
    message = message.encode('utf8')
    # connect to the SMTP server and send the email
    # be sure to replace with your smtp server
    with smtplib.SMTP("smtp.office365.com", 587) as server:
        # log in to the email account
        server.starttls()
        server.login(sender_email, passwd)
        server.sendmail(sender_email, receiver_email, message)

        print(f"Email sent to {email}")
