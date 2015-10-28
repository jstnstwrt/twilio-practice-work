##code to generate some figures of call/sms data:
setwd("~/repos/Playing-with-twilio/") #set working directory
#load required packages:
library("RSQLite")
library(DBI)


con = dbConnect(RSQLite::SQLite(), dbname="john.db") #connect to database
alltables = dbListTables(con)  #list all tables
messages = dbGetQuery( con , 'select * from message') #all info from 'messages' table
calls = dbGetQuery( con , 'select * from call') #all info from 'calls' table


####for messages
messages$pos_date <- as.POSIXct(messages$date_sent) #create 'date/time' feature
##plot number of of messages by date:
ggplot(messages , aes( x = pos_date)) +
  geom_bar() + xlab("date of messages") + ylab("number of messages")
#also see here: http://matpalm.com/blog/2012/03/18/ggplot_posix_cheat_sheet/

####for messages
calls$pos_date <- as.POSIXct(calls$date_sent) #create 'date/time' feature
##plot number of of messages by date:
ggplot(calls , aes( x = pos_date)) +
  geom_bar() + xlab("date of calls") + ylab("number of calls")
#also see here: http://matpalm.com/blog/2012/03/18/ggplot_posix_cheat_sheet/