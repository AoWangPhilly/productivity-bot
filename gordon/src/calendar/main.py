# Name: Joey Huang
# Date: 1/22-23/2021
# File: main.py
# Description: Basic Python script using the calendar module that allows the 
# user to scroll back and forth displaying different months. Loops until 
# user enters STOP.

import calendar

def printCalendar(intYear, intMonth):
    print(calendar.month(intYear,intMonth))    
    print("< | >\n")
    print(">>> Enter STOP to exit...\n")

if __name__ == "__main__":
    print("=================================================================")
    print(">>> Welcome to your interactive calendar! Are you ready to start?")

    # Not case sensitive
    reply = input(">>> Enter YES or NO: \n")
    if reply.lower() == "yes" or reply.upper() == "YES":
        year = int(input("Enter year: \n"))
        month = int(input("Enter month: \n"))
        printCalendar(year, month)
        reply = input()

        # Loops until STOP/stop is entered
        while not(reply.lower() == "stop" or reply.upper() == "STOP"):
            if reply == "<":
                # Accounts for January and December respectively
                if month == 1:  
                    month = 12
                    year -= 1
                else:
                    month -= 1
            else:
                if month == 12:
                    month = 1
                    year += 1
                else:
                    month += 1
            printCalendar(year, month)
            reply = input()

    elif reply.lower() == "no" or reply.upper() == "NO":
        print(">>> Good bye!")
    else:
        print(">>> Invalid response.")
    print("=================================================================")






    #print(calendar.calendar(2021,2,1,6))
    #print(calendar.month(2021,2,1,1))