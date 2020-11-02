from my_email import Email

e = Email()
e.sender = 'bhy0512@gmail.com'
recv_list = ['1@gmail.com', '2@gmail.com', '3@gmail.com']

for recv in recv_list:
    e.send_mail(recv, 'Welcome!', 'This is contents')