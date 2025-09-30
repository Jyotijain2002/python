# dict: use to store data into key value pair
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

d1={
    "name":"jyoti jain",
    "age":22,
    "year":2002,
    "education":"Btech",
    "year":2023
}
# first dict dont allow duplicate values but we have defined two same keys in dict the key will have later value

print(d1)

d1["year"]=2025
print(d1)

print(len(d1))
print(type(d1))
print(type({})) #op: dict

#constructing dict using constructor
d2=dict(
    fname="jyoti",
    lname="jain"
)
print(d2)

# acessing dict items
# 1) using key 
print(d2["fname"])

#2) get()  method
print(d2.get("fname"))

# 3) keys() method gives the list of keys in dict
print(d2.keys())

# 4) values() method gives all values list in dict
print(d2.values())

# 5) items() method return each item in dict as tuples in a list
print(d2.items())

if "model" in d2:
    print("yes")
else:
    print("no")


# change dictionary items
#using keys
dict1={
     "name":"jyoti jain",
     "college":"GWECA",
     "rno":53,
     "branch":"cse"
     }
dict1["rno"]="22cse053"
print(dict1)


#using update() method
dict1.update({"branch": "CSE"})
print(dict1)

# adding items
# 1. can be done by using a new index key and assigning a value to it
dict1["cgpa"]=8.71
print(dict1)

#2. using update() method
dict1.update({"placed":"Yes"})
print(dict1)


#remove dictionary items
#1) using  pop(key) method
dict1.pop("college")
print(dict1)

#2) pop_item() method : it remove the items from the end of the dict
dict1.popitem()
print(dict1)

#3) using del keyword
#del dict1
# print(dict1) 

# 4) using clear() we can empty the dict
# dict1.clear()
# print(dict1) # return {}


# loop dictionary
for x in dict1:
    print(x)

print('\n')

for x in dict1.keys():
    print(x)
print('\n')

for x in dict1.values():
    print(x)
print('\n')

for item in dict1.items():
    print(item) # returns tuple of key value pair


# copy a dict: you can just write to copy dict1=dict2 it will only refernce dict1 to dict2
# to copy a dict we use copy() method
dict2=dict1.copy()
print(dict2)
print(dict1)

# or we can copy dict using dict() constructor

dict3=dict(dict1)
print(dict3)

#nested dictionaries

dd={
    "dd1":{
        "name":"jj",
        "age":22,
        "branch":"cse"
    },
    "dd2":{
        "name":"taniya",
        "age":21,
        "branch":"cse"
    },
    "dd3":{
        "name":"sana",
        "age":21,
        "branch":"cse"
    }
}

# accessing items from nested dict
print(dd["dd1"]["name"])

for x, obj in dd.items():
    print(x)
    for y in obj:
        print(y)