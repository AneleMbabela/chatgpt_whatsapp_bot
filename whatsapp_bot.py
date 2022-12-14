
from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Your WhatsApp number
whatsapp_number = 'whatsapp:+14155552345'

# Set up a handler for incoming messages
def handle_incoming_message(message):
    # Send an automatic response
    response = client.messages.create(
        body='Thank you for your message! We will get back to you soon.',
        from_=whatsapp_number,
        to=message.from_
    )

# Set up a webhook to listen for incoming messages
message_webhook = client.webhooks.create(
    endpoint='https://example.com/handle_message',
    endpoint_method='POST',
    event_type='incoming_message',
    handler_function=handle_incoming_message
)

print(message_webhook.sid)
