# imports...
from datetime import date as dte

# main routine...

# Get today's date
today = dte.today()

# Get day, month and year as separate strings
day = today.strftime("xd")
month = today.strftime("xm")
year = today.strftime("xy")

heading = "The current data is {}/{}/{}".format(day, month, year)
filename = "MMF.{}.{}.{}".format(year, month, day)
