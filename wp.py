
'''import os
from twilio.rest import Client

client = Client()
from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+8291105704'
client.messages.create(body='hii viresh',
                       from_ = from_whatsapp_number,
                        to = to_whatsapp_number)'''



# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC33d091e217ab0caf0659e1339dd8ab9b'
auth_token = 'fab17024d6361bab4f9080fccccf477d'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body='Hello, there!',
                              to='whatsapp:+919819191672'
                          )

print(message.sid)