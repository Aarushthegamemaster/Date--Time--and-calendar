import random
import time

def RndmDate(startdate,enddate):
    print("The random day is going to be from", startdate,"to", enddate)
    randomgenerator = random.random()
    dateformat = '%m/%d/%Y'
    
    starttime = time.mktime(time.strptime(startdate,dateformat))
    endtime = time.mktime(time.strptime(enddate,dateformat))

    randomtime = starttime + randomgenerator * (endtime - starttime)
    randomdate = time.strftime(dateformat, time.localtime(randomtime))
    return randomdate

print("Random date:", RndmDate("1/1/2016", "12/12/2018"))