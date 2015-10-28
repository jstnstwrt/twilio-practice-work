##code to generate some figures of call/sms data:
setwd("~/repos/twilio-practice-work/") #set working directory
#load required packages:
library(ggplot2)
library("RSQLite")
library(DBI)
source("locations.R") #includes get_country & get_loc(ation) functions: essential!!


con = dbConnect(RSQLite::SQLite(), dbname="john.db") #connect to database
alltables = dbListTables(con)  #list all tables
messages = dbGetQuery( con , 'select * from message') #all info from 'messages' table
calls = dbGetQuery( con , 'select * from call') #all info from 'calls' table



messages <- get_country( messages) #add 'country' column
messages <- get_loc( messages)#add 'state' column

calls <- get_country(calls)#add 'country' column
calls <- get_loc(calls)#add 'state' column



##################################
###plot by state
##################################

m1 <- subset(messages , messages$country == "USA") #subset of messages from USA

#now plot:
qplot(c(calls$loc,m1$loc)) + xlab("state") + ylab("number of responses (calls & smses)") +
  theme(axis.text=element_text(size=24 , face = "bold"),
        axis.title=element_text(size=24,face="bold"))

##################################
####timeline for messages
##################################

messages$pos_date <- as.POSIXct(messages$date_sent) #create 'date/time' feature
##plot number of of messages by date:
ggplot(messages , aes( x = pos_date)) +
  geom_bar() + xlab("date of messages") + ylab("number of messages") +
  theme(axis.text=element_text(size=24 , face = "bold"),
        axis.title=element_text(size=24,face="bold"))
#also see here: http://matpalm.com/blog/2012/03/18/ggplot_posix_cheat_sheet/


##################################
####timeline for calls
##################################
calls$pos_date <- as.POSIXct(calls$date_sent) #create 'date/time' feature
##plot number of of messages by date:
ggplot(calls , aes( x = pos_date)) +
  geom_bar() + xlab("date of calls") + ylab("number of calls") +
  theme(axis.text=element_text(size=24 , face = "bold"),
        axis.title=element_text(size=24,face="bold"))
#also see here: http://matpalm.com/blog/2012/03/18/ggplot_posix_cheat_sheet/

##################################
##combined responses hist
##################################
qplot(c(calls$from_number,messages$from_number)) + xlab("phone number") + 
  ylab("number of responses (calls & smses)") + theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
  theme(axis.text=element_text(size=24 , face = "bold"),
        axis.title=element_text(size=24,face="bold"))



##################################

###scratch notes here:
calls$country <- rep(NA , length(calls$id))


for (i in 1:length(calls$id)){
  #print(i)
  if (substr( calls$from_number[i] , 2 , 2) == "1"){
    calls$country[i] = "USA"
  }
}

length( unique( c(calls$from_number , messages$from_number) ) )



substr( messages$from_number , 3 ,5 )



subset( ac_us , code == 203)





x <- subset( ac_us , code == substr( messages$from_number[2] , 3 ,5 ))
x$Area

typeof(calls$from_number[1])

substr( messages$from_number , 2 , 2)
