# print even and odd numbers
odd=[]
even=[]
for num in range(11):
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)

print(odd, even)
odd.clear()
even.clear()


i=0
while i<=10:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
    i+=1

print(even, odd)

i=0
while i<=10:
    if i==0 or i==1 or i==10:
        i+=1
        continue
    else:
        print(i, end=" ")
    i+=1 
print('\n')

# break statement
num=[12,34,78,34]
for i in num:
    if i==78:
        break
    else:
        print(i, end=" ")
print('\n')

string="i am jyot jain"
char=[]
for ch in string:
    char.append(ch)

print(char)


#range method : range(start, end+1, increament/decrement/updation)

for i in range(0,11,2): # increament=> i+=2
    print(i)