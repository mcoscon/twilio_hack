from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv()
#uncomment this and @run_once to run once
def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper


@run_once
def send_twilio(url):

    # Your Account SID from twilio.com/console
    account_sid = os.getenv("TWILIO_SID")
    # Your Auth Token from twilio.com/console
    auth_token  = os.getenv("TWILIO_AUTH")
    client = Client(account_sid, auth_token)
    message = client.messages \
    .create(
         ##media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80'],
         #media_url=["http://res.cloudinary.com/cl0ud123/image/upload/human"],
         media_url=[url[0]],
         from_='whatsapp:+14155238886',
         body="Someone just broke into your room!",
         to='whatsapp:+601136776256'
     )
    print(message.sid)