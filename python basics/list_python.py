#list is used to store multiple items in a single variable
#lists are ordered, these are changable means we can change, add, and remove items from list
#allow duplicates, list items can be of any datatype

list1=[23, "mango",56.90,True]
for element in list1:
    print(element)

print(list1)
print(list1[0])
print(type(list1))
print(len(list1))

list1[0]=2345
print(list1)

list2=[]
print(list2) #empty list
print(type(list2))


list3=list(("janeman","lovely",4,457678.898))
print(list3)
print(type(list3))
# list() constructor can also be used to create list 
#we can do negative indexing also

print(list3[2:3]) # we can do list slicing also


print(4 in list3) #True


#change a range of items in list

list3[:5]=["DDLJ","kkkG","dilwale","jaana","tyty"]
print(list3)

#insert in list

list3.insert(3,52376.909) #insert add element in list at a specified index 
print(list3)

list3.append(4325624) #appned the element at the end of the list
print(list3)


#extend appends element from another list to current list. it can also append tuples ,set , dictionaries in list
l1=[623,"hdeh","heuwy",52435.87]
l2=[535,"hsdgh","wfee",True]
l1.extend(l2)
print(l1)
print(l2)

#remove method
l1.remove(623) # it will remove the specified element if it is present in the list else it will error
print(l1)

#remopve specified index
l1.pop(-1) #will remove ele at index -1 here it is "True"
print(l1) 

#del keyword remove element at a specified index
del l1[4]
print(l1)

#it can also delete whole list
del l2
# print(l2) will give error l2 is not defined because we have deleted it


#clear method
l1.clear()
print(l1) #return empty l1 []



#looping over list
print('\n')
my_list=["hello","hii","bye-bye","lol","tata","lala"]

for el in my_list:
    print(el)
print('\n')

for i in range(len(my_list)):
    print(my_list[i])

print('\n')

i=0
while i<len(my_list):
    print(my_list[i])
    i+=1
print('\n')


#looping using list comprehension: it offers the shortest synax for looping
print('looping comprehension\n')
[print(x) for x in my_list]
print('\n')
fruits=["banana","mango","cherry","lichi","falsa","sugarcane"]
new_list=[]

[new_list.append(x) for x in fruits]
print(new_list)

newl=[x for x in range(10)] #(0-9)
print(newl)
new_fruits=[x.upper() for x in fruits]
print(new_fruits)

[newl.remove(x) for x in newl if x==1]
print(newl)

#syntax: newlist = [expression for item in iterable if condition == True]

#list sort

my_list1=["banana","apple","apollo","aajtak","zebra"]
my_list1.sort()
print(my_list1)

#sort in descending order use keyword reverse=true
my_list1.sort(reverse=True)
print(my_list1)

#customize sort function

def myfunc(n):
    return abs(n-50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# reverse() : this method helps us to reverse the list
thislist.reverse()
print(thislist)

#copy a list
#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2. so that's why we use copy() method

list1=[27,38,3256,76,367]
list2=list1.copy()
print(list2)
list1.append(678566)
print(list1," ",list2)


# another way to copy a list is using list() constructor
list3=list(list1)
print(list3)
# or you use slice operator
list4=list1[:]
print(list4) 


# join (+): this operator is used to concatenate two or more lists or you can use extend() method
l1=["a","b","d","e"]
l2=["c","f","g","h"]
l3=l1+l2 #use of join operator
print(l3)
