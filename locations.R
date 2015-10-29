#source geo-library
ac <- read.csv("globalareacodes.csv")
ac_us <- subset( ac , Country == "United States") #isolate subset consisting of US area codes
ac_us$code <- substr(ac_us$Area.Code, 5, 7 ) #add area codes as column


##get country

get_country <- function(df){
  ##requires column df$id
  df$country <- rep(NA , length(df$id))
  for (i in 1:length(df$id)){
    #print(i)
    if (substr( df$from_number[i] , 2 , 2) == "1"){
      df$country[i] = "USA"
    } 
    if (substr( df$from_number[i] , 2 , 3) == "61"){
      df$country[i] = "AUS"
    }
  }
  
  return(df)
}

###area codes

get_loc <- function( df ){
  ##requires column df$id
  df$loc <- rep(NA , length(df$id))
  for (i in 1:length(df$id)){
    #print(i)
    x <- subset( ac_us , code == substr( df$from_number[i] , 3 ,5 ))
    #print(x$Area)
    df$loc[i] <- toString(x$Area)
  }
  return(df)
}