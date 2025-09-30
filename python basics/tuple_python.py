#tuple:is a collection which is ordered and unchangable and allow duplicate values

tuple1=("banana","apple","mango","orange")
print(tuple1)
print(type(tuple1))

t1=() #empty tuple
print(type(t1)) # <class tuple>

#tuple items are indexed from 0 to size-1
# tuple are unchangable means we cannot add,remove and change values in tuple

# tuple1[0]="strawberry"
# print(tuple1) will give error beacuse tuple dont support item assignment\

print(len(tuple1))
print(tuple1[0])
 

#Create Tuple With One Item
t2=("apple")
print(type(t2))  # will give str as type

#so to make one element tuple, you have to add a comma after the item else python will not consider as tuple
t3=("apple",)
print(type(t3)) # type: tuple

#tuple can contain different data types
t4=("apple","zebra",34,True,89.98)
print(t4)

#creating tuple using tuple constructor
t5=tuple(("mango","jivan",90))
print(t5)

#creatin one element tuple using tuple constructor
t6=tuple(("apple"))
print(type(t6))  # type: tuple


#accessing tuple element: 1) using index (positive or negative)
my_tuple=('english',"pratibha","sundar",4567,729,True)

print(my_tuple[0]," ",my_tuple[-1])
 
#tuple slicing
print(my_tuple[2:5])

#check if an item is present in tuple or not
if 'english' in my_tuple:
    print("yes english is present")
else:
    print('not present')


#we know that tuples are unchangable so how can we update tuple
#so for doing this first we will convert tuple into list and then update

tuple2={'hello',"welcome","hii","what's up"}
list1=list(tuple2)
list1.remove('hello')
list1.append('ram ram')
list1.sort()
tuple2=tuple(list1)
print(tuple2)
print(type(tuple2))


# del keyword is used to delete a tuple
del tuple2
# print(tuple2) will give error beacause we have already deleted the tuple2 
# so it will give undefined error


#packing: when we craete a tuple , we normally assign values to it is called packing
#unpacking: reverse of packing , extracting values back into variable

tuple3=(1,2,3,4,5)
(num1, num2, num3,num4,num5)=tuple3
print(num1,num2,num3,num4,num5)
#(x,y,z)=tuple3
# print(x,y,z) will give error as we must unpack all the elements of the tuple together
#Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.


# we can also do list unpacking
list1=[1,2,3]
[one,two,three]=list1
print(one,two,three)


tuple4=('jj',"hj","rj","jaya")
(one, two, *other)=tuple4
# here all the remaining element will be stored in the other list
print(one, two, other)
print(type(other))



#loops through tuple

t23=(1,2,3,4,5)
for el in t23:
  print(el,end=" ")
print('\n')


#loop through index number
for i in range(len(t23)):
    print(t23[i],end=" ")
print('\n')

# while loop
i=0
while i<len(t23):
    print(t23[i],end=" ")
    i+=1

print('\n')
#join two tuple using + operator but here we cant use extend() method as tuple are unchangable

a=(1,2,3)
b=(3,4,5)
c=a+b
print(c)
print('\n')

#multiply tuple:If you want to multiply the content of a tuple a given number of times, you can use the * operator:
d=a * 3
print(d)  #op: (1, 2, 3, 1, 2, 3, 1, 2, 3) all the values of a will be repeated 3 times


#tuple methods

print(d.count(1)) # op:3
print(d.index(1)) # op:0 index return first occurence index of the given value
