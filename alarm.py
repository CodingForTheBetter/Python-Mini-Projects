#install important libraries
#pip install datetime
#pip install playsound

# Importing required libraries
from datetime import datetime   #To set date and time
#from playsound import playsound #To play sound


def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid HOUR format! Please try again..."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format! Please try again..."
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Please try again..."
        else:
            return "ok"

#validate_time is the name of our function. Let's dissect it and figure out what's going on -
#As a parameter alarm time, our function allows user input.
#We verify the length of user input to be precisely 11 characters in the first if statement at len(alarm time)!= 11. 
#If this is not the case, a statement will be returned, requesting the user to re-enter the value.

#If the user input is precisely 11 characters long, the otherwise block will run; this is where our user input will be validated more thoroughly.
#The first two letters of our input, HH, are validated in the first if statement within the else block. 
#There is a risk that the user will enter incorrect hour values, such as anything longer than 12 hours.
#If you scroll down you will see a segment of code that looks like this, ' current_hour = now.strftime("%I") ',
#by chnaging the %I to %H, this allows the user to input 24 hour time formats which means the 'current_period' variable isn't needed.

#We're accessing the first two characters of user input using a slicing operator at alarm time[0:2]. 
#If the duration of the input is less than 12 hours, the execution will proceed to the following conditional expression. 
#However, if the time input exceeds 12 hours, it will send a message requesting the user to re-enter the time.

#The next two conditional statements perform the same thing as the first, comparing minutes and seconds.
#If all of the input is correct, our function's 'else' block will return OK. This is when our task as a function comes to an end.

while True:
    alarm_time = input("Enter time in 'HH:MM:SS AM/PM' for example: 07:22:05 pm (ensure space between the SS and the AM/PM) format: ")
    
    validate = validate_time(alarm_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}...")
        break

#Here is where we call our validate_time function ^
#Here we are storing the output of the function into a variable validate which we are using to judge whether the input is valid or not. If it is not valid then the user will be prompted to enter the time again. 
#If not then the execution will head to the next step.
#Now that we are sure the input provided by the user is valid, we can now separately store the values into different variables like shown below:

alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()

#We make use of some slicing here. Here we are using slicing operator to store the specific unit of time into specific variables. 
#HH will be stored in alarm_hour, MM in alarm_min and so on.

while True:
    now = datetime.now()

    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")

#Do you recall the datetime module we loaded at the beginning of our project?  We'll finally put it to good use. To begin, we'll use datetime. We use now() to get the current time and save it in the now variable.
#Next, we'll extract particular time data from the now variable using % notation.
#This is quite similar to the user input we just performed.  For comparison, now.strftime() is applied to the string formatted data.

    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("Wake Up!")
                    #playsound('C:/Users/tanus/Downloads/blue_monday-freemobi.mp3')
                    break