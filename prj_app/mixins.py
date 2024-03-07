from django.conf import settings
from twilio.rest import Client
import random
class MessaHandler:
    phone=None
    otp=None
    def __init__(self,phone,otp)->None:
        self.phone=phone
        self.otp=otp

    def send_otp_on_phone(self):
        client=Client(settings.ACCOUNT_SID,settings.AUTH_TOKEN)
        message=client.messages.create(body=f'Your otp is',from_='+19896324797',to=self.phone)

# Provide your Twilio Account SID and Auth Token here
settings.ACCOUNT_SID = 'AC237fd83b9e149d213c7adc880e818de9'
settings.AUTH_TOKEN = 'e122fe078ba029945b31fd73b7048eb7'

# Example phone number and OTP
phone_number = '+1234567890'
otp = ''.join(random.choices('0123456789', k=6))

# Create an instance of MessageHandler
message_handler = MessageHandler(phone_number, otp)

# Send OTP message
message_handler.send_otp_on_phone()

print("OTP message sent successfully!")