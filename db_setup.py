import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Message(Base):
	__tablename__ = 'message'

	id = Column( Integer, primary_key = True)
	twillio_id = Column( String(80) ,unique = True, nullable =  False)
	from_number = Column( String(80) , nullable = False)
	to_number = Column( String(80), nullable = False)
	date_sent = Column( String(80) ) 
	body = Column( Text )
	direction =  Column(String(80))

class Call(Base):
	__tablename__ = 'call'

	id = Column( Integer, primary_key = True)
	twillio_id = Column( String(80) ,unique = True, nullable =  False)
	from_number = Column( String(80) , nullable = False)
	to_number = Column( String(80), nullable = False)
	date_sent = Column( String(80))
	direction =  Column(String(80)) 

engine = create_engine('sqlite:///john.db')
Base.metadata.create_all(engine)