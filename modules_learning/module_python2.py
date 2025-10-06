# we can choose to import only parts from a module,by using "from" keyword

from mymodule1 import person1 as p1 ,list1 as l1
print(p1)
print(l1) 

for values in p1.values():
    print(values,end=" ")

print('\n')

l1.append("jyoti jain")
print(l1)

