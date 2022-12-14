from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Your WhatsApp number
whatsapp_number = 'whatsapp:+14155552345'

# The distribution list
distribution_list = ['whatsapp:+15551234567', 'whatsapp:+15557654321']

# Send the message to the distribution list
for recipient in distribution_list:
    message = client.messages.create(
        body='Hello, this is a message from my WhatsApp bot.',
        from_=whatsapp_number,
        to=recipient
    )

    print(f'Sent message to {recipient} with SID {message.sid}')
