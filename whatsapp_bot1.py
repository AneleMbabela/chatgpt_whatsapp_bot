
from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Your WhatsApp number and the customer's number
whatsapp_number = 'whatsapp:+14155552345'
customer_number = 'whatsapp:+15551234567'

# Send the message
message = client.messages.create(
    body='Hello, how can I help you?',
    from_=whatsapp_number,
    to=customer_number
)

print(message.sid)