import datetime


class Message(object):

    def __init__(self, text, author, recipient):
        self.created = datetime.datetime.now()
        self.text = text
        self.author = author
        self.recipient = recipient

    def get_info(self):
        print(self.text)
        print(self.created.strftime("%d.%m.%Y %H:%M"))


message = Message('fdsfsd', 'User', 'User2')
message.get_info()
