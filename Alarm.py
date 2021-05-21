# Edit the address of desired alarmtone; if error, try another mp3, could be bitrate problem
#datetime has many libraries like date, time, datetime, timedelta. we have only imported Datetime
# Use ctrl+C to break

from datetime import datetime
from playsound import playsound

print("Hello,please enter time to set up alarm")
a= input("\nEnter hour: ")
b= input("\nEnter minute: ")
alarm_hour= int(a)
alarm_min= int(b)
print("Alarm set!!!")

while True:
    x=datetime.now()
    hour=x.hour
    minute=x.minute
     
    if(alarm_hour==hour):
        if(alarm_min==minute):
            print("WAKE UP")
            playsound('C:/Users/Abhinav/Music/08-Waiting-For-The-End.mp3')
            break
    elif(alarm_hour<hour):
        print("Past time- Invalid")
        break