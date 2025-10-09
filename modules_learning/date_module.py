'''
Python Dates
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
'''

import datetime 

x=datetime.datetime.now().date().day
print(x)
x=datetime.datetime.now()
print(x.year)
print(x.ctime())
print(x.hour)
print(x.second)



# creating date objects

y=datetime.datetime(2002,11,10)
print(y)

'''
strftime() method: it takes one parameter, format to specify the format of the returned string

some of the legal format codes:
%a = weekday,short version
%A = weekday,full version
%w = Weekday as a number 0-6, 0 is Sunday
%d = Day of month 01-31
%b	Month name, short version
%B	Month name, full version
%m	Month as a number 01-12
%y	Year, short version, without century
%Y	Year, full version
%H	Hour 00-23
%I	Hour 00-12
%p	AM/PM
'''

print(y.strftime("%B"))
