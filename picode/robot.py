import datetime
import os

# Collected dates dict
collected_days={}
collected_days['no_smoking_date']=datetime.date(2017,9,30)
collected_days['Tibet5start']=datetime.date(2017,10,11)

# Display Dates
os.system('clear')
for day in collected_days.keys():
    print(day+"\t",(datetime.date.today()-collected_days[day]).days)
print("\n\n\n")

message=input("quit/repeat me/\n")
while True:
    if message=="quit":
        break
    elif message=="repeat me":
        print(message)
        message=input("Now, what?")
    else:
        message=input("No-sense, again pls:\n")
