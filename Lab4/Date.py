import datetime 

#1. Write a Python program to subtract five days from current date.
def fiveDaysAgo():
    today = datetime.date.today()
    fiveDays = datetime.timedelta(days=5) #found the object in docs

    print("Output:", today - fiveDays)


#2. Write a Python program to print yesterday, today, tomorrow.
def pastPresentFuture():
    today = datetime.date.today()
    oneDay = datetime.timedelta(days=5)

    print(f"Yesterday: {today-oneDay} \nToday: {today} \nTomorrow: {today+oneDay}")


#3. Write a Python program to drop microseconds from datetime.
def dropMicroseconds():
    today = datetime.datetime.now()
    msecs = datetime.timedelta(microseconds=int(today.strftime("%f")))

    print("Output:", today - msecs)


#4. Write a Python program to calculate two date difference in seconds.
def differenceInSeconds():
    someDay = datetime.date(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")))
    today = datetime.date.today()

    print("Difference in seconds:", abs(today - someDay).total_seconds()) 


#Testing

differenceInSeconds()
