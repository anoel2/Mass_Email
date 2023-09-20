# What it is for
This takes an array of e-mail addresses, and sends an e-mail to each, while also including the e-mail of each user in the body. This, allows for an individual user to receive a personalized e-mail, where their e-mail is the username, but not all e-mails are in the same formatting. Thus, giving a unique result to each user.

I.e. an organization has multiple e-mail formats, for various reasons. Legacy names, etc. xyz@example.com, and x.y.z@example.com. 

# How to use
Update email_list.py with a list of e-mails you wish to send in the form of an array. 
Update the name of the Subject and SMTP server you wish to use in email_send.py, 
Update the message body in message.py. 
In smtp_secret.py, add you credentials. It is already in gitignore.  

# Example Output

With the Array set to ["usera@example.com","userb@example.com"]

~ Let the for loop do the for loop stuff. Iterate and what-not. ~

Message body: 

"Hello, your username is {email} please use this for login to the new system." 

User A recieves: 
"Hello, your username is usera@example.com please use this for login to the new system." 

User B recieves: 
"Hello, your username is userb@example.com please use this for login to the new system"
