#set : A set is a collection which is unordered, unchangeable*, and unindexed and duplicates are not allowed.
# * Note: Set items are unchangeable, but you can remove items and add new items.

myset={"apple","banana",True}
print(myset)
myset.add("apple")
print(myset)  #it will not give error but won't show duplicate items
myset.remove("apple") # it will remove apple from myset
print(myset)

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates. similarly for false and 0

myset.add(1) # it will not add 1 in myset because True is already present in myset
print(myset)

#length of set
print(len(myset))

#set items can be of any datatype
s1={"fruits",1,90.78,"jyoti"}
print(s1)


#createing empty and one element set
s2={}
print(type(s1))

s3={23}
print(type(s3))

#creating set using set constructor
s4=set((23,45,78))
print(s4)


# access set items
# 1-method: using for in loop
for el in myset:
 print(el,end=" ")


 # set_name.add(ele_value) is used to add items in set
 # set_name.remove(ele_value) is used to remove items from set


 #add sets: to add items from another set into the current set , use update() method
#you can add any iterable using update() method
set1={1,2,3}
set2={5,8,7}

set1.update(set2) # set1 will haqve all the values of set2 except duplicates
print(set1, set2)

t1=(23,True, "java")
set1.update(t1)
print(set1)
print(type(set1)) #set

# remove set items: to remove set items use the remove() method or discard() method

set2={23, 34,"Taniya",1+5j,12,45}
print(set2)
# set2.remove(1) 1 is not present in set2 so it will give error
set2.discard(1) # even if the element is not present in set2 it will not give error 
print(set2)


# pop() method : this method also used to remove element from set but it removes random element from the set

set2.pop()
print(set2)

# clear(): method it empties the set
set2.clear()
print(set2) # op: set()  

# del keyword will delete the set completely
del set2
# print(set2) # will give error that set2 is undefined


#loops on set
set2={"hello","hii","welcome","Gm"}

for x in set2:
 print(x, end=" ")
print('\n')


# we cannot use while loop on set

#join sets method
# 1) union() and update(): joins all the items form both sets
set11={1,12,8,9,5,4}
set21={23, 1, 45, 9,8,7}

set31={}
print(type(set31)) #type: Dict
set41=set() #correct way to create empty set
set41.update(set11)
print(set41)

# 2) intersection(): keeps only duplicates
set51=set11.intersection(set21)# will contain duplaicates in present in set11 and set21
print(set51) 
print(set11) #no change in set11


# 3) difference() method: keeps the items from the first set that are not in the other set(s).

set61=set11.difference(set21)
print(set61)

# 4)  The symmetric_difference() method keeps all items EXCEPT the duplicates.

set71=set11.symmetric_difference(set21)
print(set71)

#if we put udate behind this set operation then changes will made in the set on which operations are performed
#like : union_update(), symmetric_difference_update() etc


# join multiple sets
s11={1,2,3}
s22={"qa","b","c"}
s33={True, False}
s44=s11.union(s22,s33)
print(s44)

# we can also join a set with mutiple set using "|" operator but cant be used to join a set with tuple and list

s55=s11 | s22 | s33| s44
print(s55)

# you can use "&" operator for intersection but can only used for set with set

s66= s11 & s22 & s33 & s44 & s55
print(s66)

# you can use "-" operator for diffrence but only used for sets
s77=s11-s22
print(s77) 

# for symmetric_difference we can use "^" operator but only applicable for sets
s88=s11^s22
print(s88)