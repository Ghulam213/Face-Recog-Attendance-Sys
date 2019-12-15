import os
from twilio.rest import Client

acc_sid = os.environ.get('ACC_SID')
auth_token = os.environ.get('AUTH_TOKEN')
my_number = os.environ.get('MY_PHONE_NUMBER')

client = Client(acc_sid, auth_token)


client.messages.create(
    to=my_number,
    from_=+18597554541,
    body='Please report to the class or you will not be marked present.'
)