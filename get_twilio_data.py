from config import * 
from twilio.rest import TwilioRestClient
from models import store_call,  store_john, does_john_exist, update_john_message_count
from db_setup import John

# Configuration
# Account Sid and Auth Token from twilio.com/user/account
account_sid = ACCOUNT_SID #insert id here
auth_token  = AUTH_TOKEN #insert token here
client = TwilioRestClient(account_sid, auth_token)


# A list of message objects with the properties described above
messages = client.messages.list()
calls = client.calls.list()
#http://twilio-python.readthedocs.org/en/latest/usage/messages.html

for m in messages:
	update_john_message_count(m.from_)

# for c in calls:
# 	store_call(c)


