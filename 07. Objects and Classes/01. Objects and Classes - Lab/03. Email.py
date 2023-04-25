class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


mailbox = []
command = input()
while command != "Stop":
    command = command.split()
    sender = command[0]
    receiver = command[1]
    content = command[2]
    email = Email(sender, receiver, content)
    mailbox.append(email)

    command = input()

index = list(map(int, input().split(", ")))

for x in index:
    mailbox[x].send()

for mail in mailbox:
    print(mail.get_info())
