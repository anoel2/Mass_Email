# What it is for
This takes an array of e-mail addresses, and sends an e-mail to each, while also including the e-mail of each user in the body. This, allows for an individual user to receive a personalized e-mail, where their e-mail is the username, but not all e-mails are in the same formatting. Thus, giving a unique result to each user.

I.e. an organization has multiple e-mail formats, for various reasons. Legacy names, etc. xyz@example.com, and x.y.z@example.com. 

# How to use
In email.py, you need to update the e-mails array with your list of addresses, update the name of the SMTP server you wish to use, and fillout the message body and subject. 

In smtp_secret.py, add you credentials. 


# Example Output

With the Array set to ["usera@example.com","userb@example.com"]

~ Let the for loop do the for loop stuff. Iterate and what-not. ~

Message body: 

"Hello, your username is {email} please use this for login to the new system." 

User A recieves: 
"Hello, your username is usera@example.com please use this for login to the new system." 

User B recieves: 
"Hello, your username is userb@example.com please use this for login to the new system"
