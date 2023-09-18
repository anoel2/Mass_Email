import smtplib
from smtp_secret import password
passwd = password
emails = ["list","of","addressess"]
for email in emails:
    sender_email = "<replace with sender_email address"
    sender_display_name = "<Desired Display Name>"
    receiver_email = email
    reply_to_email = "<replace with reply-to email address>"
    message = f"""Subject: Example
    From: {sender_display_name} <{sender_email}>
    Reply-To: {reply_to_email}
      
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
