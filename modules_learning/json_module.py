'''
json is a syntax for storing and exchanging data
json is text, written in javascript object notation

json in python:
python has a built-in package called json, which can be used to work with json data
'''

import json

'''
parse json-convert from json to python
if we have a json string, we can parse it by using json.loads() method
ans result will be python dictionary
'''

#some json
x='{"name":"jyoti jain","age":30,"city":"new-york"}'
print(type(x))

#parse x
y=json.loads(x)
print(type(y))

print(y["name"])


'''
covert from python to json
if you have python object, you can convert it into a json string by using the 

json.dumps()
method

::You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None

'''

list1=[1,2,3,4]
json1=json.dumps(list1)
print(json1)
print(type(json1)) # str

tuple1=("hello",34.56,True)
print(type(json.dumps(tuple1))) #str

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))


'''format the result:
the above example prints a json string,but it is not very easy to read, with no identations and line breaks.
The json.dumps() method has parameters to make it easier to read the result: that is <indent>
'''
print(json.dumps(x,indent=4))


'''
You can also define the separators, default value is (", " , ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:
'''

print(json.dumps(x,indent=4,separators=(". "," = ")))

'''
order the result:
the json.dumps() method has parameters to order the keys in the result
'''

print(json.dumps(x,indent=4,sort_keys=True))