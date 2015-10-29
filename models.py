from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
import sqlalchemy.exc
from db_setup import Base, Message, Call, John

engine = create_engine('sqlite:///john.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
db_session = DBSession()



def does_john_exist(number):
	(ret, ), = db_session.query(exists().where(John.number==number))
	return ret


## this is working for the mooment, but needs to be done more elegantly.
## need to store initallized values for call count and message count
def store_john(response):
	if response.__class__ == "<class 'twilio.rest.resources.messages.Message'>":
		message_count = 1
		call_count = 0
	else:
		message_count = 0
		call_count = 1
	newJohn = John(	number =  response.from_ , message_count = message_count, call_count = call_count)
	try:
		db_session.add(newJohn)
		db_session.commit()
		print "succesfully added john!"
	except sqlalchemy.exc.IntegrityError:
		print "IntegrityError"
		db_session.rollback()
    	# db_session.close()


def update_john_message_count(number):
	updatedJohn = db_session.query(John).filter(John.number==number).one()
	updatedJohn.message_count += 1
	db_session.add(updatedJohn)
	db_session.commit()
	print "succesfully updated john's message count!"

def update_john_call_count(number):
	updatedJohn = db_session.query(John).filter(John.number==number).one()
	updatedJohn.call_count += 1
	db_session.add(updatedJohn)
	db_session.commit()
	print "succesfully updated john's call count!"


def store_message(message):
	newMessage = Message(	twillio_id = message.sid,
							from_number = message.from_,
							to_number = message.to,
							date_sent = message.date_sent,
							body = message.body,
							direction = message.direction)
	try:
		db_session.add(newMessage)
		if does_john_exist(newMessage.from_number):
			update_john_message_count(newMessage.from_number)
		else:
			store_john(message)
		db_session.commit()
	except sqlalchemy.exc.IntegrityError:
		print "IntegrityError"
		db_session.rollback()
    	# db_session.close


def store_call(call):
	newCall = Call(	twillio_id = call.sid,
					from_number = call.from_,
					to_number = call.to,
					date_sent = call.date_created,
					direction = call.direction)
	try:
		db_session.add(newCall)
		if does_john_exist(newCall.from_number):
			update_john_call_count(newCall.from_number)
		else:
			store_john(call)
		db_session.commit()
		print "succesfully added call!"
	except sqlalchemy.exc.IntegrityError:
		print "IntegrityError"
		db_session.rollback()
    	# db_session.close()



