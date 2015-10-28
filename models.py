from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
import sqlalchemy.exc
from db_setup import Base, Message, Call, John

engine = create_engine('sqlite:///john.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
db_session = DBSession()


def store_message(message):
	newMessage = Message(	twillio_id = message.sid,
							from_number = message.from_,
							to_number = message.to,
							date_sent = message.date_sent,
							body = message.body,
							direction = message.direction)
	try:
		db_session.add(newMessage)
		db_session.commit()
		print "succesfully added message!"
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
		db_session.commit()
		print "succesfully added call!"
	except sqlalchemy.exc.IntegrityError:
		print "IntegrityError"
		db_session.rollback()
    	# db_session.close()


def store_john(john_number):
	newJohn = John(	number = john_number)
	try:
		db_session.add(newJohn)
		db_session.commit()
		print "succesfully added john!"
	except sqlalchemy.exc.IntegrityError:
		print "IntegrityError"
		db_session.rollback()
    	# db_session.close()