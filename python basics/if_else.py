day=int(input("enter day of week"))
# if day==0:
#     print("sunday")
# elif day==1:
#     print("monday")
# elif day==2:
#     print("tuesday")
# elif day==3:
#     print("wednesday")
# elif day==4:
#     print("thursday")
# elif day==5:
#     print("friday")
# elif day==6:
#     print("saturday")
# else:
#     print("enter correct day of week")


#short hand if: If you have only one statement to execute, you can put it on the same line as the if statement.
if 10>9: print("yeah its true")

#short hand if-else

print("lalala") if 3>=4 else print("hahaha")  #ternery operator or conditional expression

#You can also have multiple else statements on the same line:

print("hello") if 0>1 else print("love") if 1<2 else print("jaadu")


age=13
if age<16 or age>60:
    print("you cant ride it its too risky for you ")
else:
    print("are you ready to go")


#nested if

if age>=16:
    if(age>=18):
        print("you can vote")
    else:
        print("there is still time to vote")
else:
    print("you are too little to vote")


#pass statement: if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

if 23 != 45:
    pass


# here in python we case match keyword instead switch statement

match day:
    case 0:
        print("sunday")
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case _: # default case 
        print("enter correct day of week")
    

match day:
    case 1|2|3|4|5:
        print("no holiday, just work")
    case 0|6:
        print("finally weekends")
    case _:
        print("enter correct day of week")


# if statement as guards in match statement
month=6
match day:
    case 1|2|3|4|5 if month==6:
        print("work in june, not holiday today")
    case 1|2|3|4|5 if month==4:
        print("weekday in april")
    case _:
        print("maje maro")