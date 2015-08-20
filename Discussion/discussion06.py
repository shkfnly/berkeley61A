def take_color(self, color):
  for skittle in self.skittles:
    if skittle.color = color:
      return take_skittle()
  return None

def take_all(self):
  for skittle in self.skittles:
    s = take_skittle()
    print(s.color)

class Email:
  def __init__(self,msg,sender,addressee):
    self.msg = msg
    self.sender = sender
    self.addressee = addressee

class Postman:
  def __init__(self):
    self.clients = dict()
  def send(self, email):
    client = self.clients[email.addressee]
    client.recieve(email)

  def register_client(self, client, client_name):
    self.clients[client_name] = client
class Client:
  def __init__(self, mailman, name):
    self.inbox = list()
    self.name = name
    self.mailman = mailman
    self.mailman.register_client(self, self.nlame) = mailman
  def compose(self, msg, recipient):
    self.mailman.send(email(msg, self.name, recipient))

  def receive(self, email):
    self.inbox.append(email)

