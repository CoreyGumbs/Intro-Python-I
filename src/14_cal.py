"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import date

#gets date (month, year or both) from command line args
selectDate = sys.argv[1:]
#sets today's date
today = date.today()

#self-exectuting function
def newCalendar(*args):
      #if *args has no input
      if not args:
            #print usage message for proper arguments needed
            print("\n Please enter a valid month and year! Ex: python 14_cal.py 3 2020 \n")
          
            #returns calendar of the current month of the current year
            return calendar.month(today.year, today.month, 3, 1)
      #check if only one argument passed
      elif len(args) == 1:
            #assign first argument to var
            month = args[0]
            #test if month given is within range of 1-12
            if int(month) in range(1, 13):
                  #returns calendar with of given month in current year
                  return calendar.month(today.year, int(month), 3, 1)
            else:
                  #if out of range - returns a message to enter valid arguments
                  print("\n Please enter a valid month and year! Ex: python 14_cal.py 3 2020 \n")
                  #exits the program
                  sys.exit()  
      #check if two args passed           
      elif len(args) == 2:
            #assign first arg to month
            month= args[0]
            #assign second arg to year
            year= args[1]
            #return calendar of given month & year
            return calendar.month(int(year), int(month), 3, 1)

if __name__ == "__main__":
  print(newCalendar(*selectDate))