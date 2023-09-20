import smtplib
from smtp_secret import password
from email_list import emails
from message import messagebody
passwd = password
# Set up email details
sender_email = "send as address"
sender_display_name = "Display name" # replace with your desired display name
reply_to_email = "<reply to address"
subject = "Example TEST"
for email in emails:
    body = messagebody
    message_parts = [
        f"Subject: {subject}",
        f"From: {sender_display_name} <{sender_email}>",
        f"To: {email}",
        f"Reply-To: {reply_to_email}",
        "",
        body,
    ]
    message = "\n".join(message_parts).encode("utf8")

    try:
        with smtplib.SMTP("smtp.office365.com", 587) as server:
            server.starttls()
            server.login(sender_email, passwd)
            server.sendmail(sender_email, email, message)

        print(f"Email sent to {email}")
    except Exception as e:
        print(f"Error sending email to {email}: {e}")

