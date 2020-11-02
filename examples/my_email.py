class Email:
    sender = ''

    def send_mail(self, recv, subject, contents):
        print('From:\t' + self.sender)
        print('To:\t' + recv)
        print('Subject:' + subject)
        print('Contents')
        print(contents)
        print('-'*20)