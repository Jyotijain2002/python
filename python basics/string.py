name="hello world"
print(name[0]) #strings as array

#looping through a string
for char in name:
    print(char)

#string len
print(len(name))


sentence= "hi my name is jyoti jain"

#check string if a certain phrase is present in string\
print("jain" in sentence) #True
print("expression" in sentence) #False
print("expression" not in sentence) #True

if "expression" not in sentence:
    print("no expression")

    #string slicing: you can return a arnge of characters by using the string slicing
    #specify the start index and end index, separated by colon, to resturn a part 
    #of the string
print(sentence[0:5]) # 5th position not included
print(name[1:3]) # 3rd position not included
     
#slice from start
print(sentence[:5])
#slice form end
print(sentence[4:])     


#negative indexing
b="hello world"
print(b[-5:-2]) #orl
# index(positive)= (string len) - (negative index)

#modify strings

#upper case
a="hello world"
print(a.upper()) # HELLO WORLD

#lower case
b="JYOTI JAIN"
print(b.lower())

#remove whitespace: before and after the actual text
#strip() method remove whitespaces from begining or end
x="   lalaalla  herllo world   "
print(x.strip())


#replace string: replace() method replace a string with another string
a="hello world"
print(a.replace("hello","jyoti")) # jyoti world


# split() method splits the string into substrings if it findes instances 
# of separator
a="hello world welcome back"
print(a.split(" ")) # ['hello' , 'world' ,'welcome', 'back'] 



#string concatenation
a="jyoti"
b="jain"
c=a+b
d=a+" "+b
print(c,"\n",d)


#format strings
#as we know that in python we cannot combine strings and numbers using "+" operator
#but we can combine them using f-strings
#to specify a string as a f-string, simply put an f in front of the string 
# literal and add curly brackets {} as a placeholder for variables and other opperations

age=18
print(f"hii my name is jyoti and my age is {age}")

#fstrings can be used as placeholder and modifier, place holder can contain 
#variables, operations, functions, and modifiers to format the value.
#A placeholder can include a modifier to format the value.

#A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

print(f"hey can you convert my age in decimal yes here it is {age:.2f}")
print(f"the multipliaction operation {56*34 : .2f}")

# we can perform if-else statement inside the placeholder
price=67
txt=f"it is very {'expensive' if price>50 else 'cheap' }"
print(txt)


# can also call function inside a placeholder

def my_doubler(x):
    return 2*x

txt=f"due to inflation the price of rice is doubled up by {my_doubler(45)} per kg"
print(txt)


# format() method:The format() method can still be used, but f-strings are faster and the preferred way to format strings.
# The format() method also uses curly brackets as placeholders {}, but the syntax is slightly different:
# we can give multiple values using format mrthod

txt= "the price is {} dollars"
print(txt.format(49))

txt="hey my name is {} and my age is {}"
print(txt.format("jyoti jain",22)) #op: hey my name is jyoti jain and my age is 22

'''
Index Numbers
You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
'''
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

'''
Named Indexes
You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):
'''
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))