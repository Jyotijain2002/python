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

