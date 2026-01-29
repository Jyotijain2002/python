'''
A regular expression, is a sequence of characters that forms a search pattern.
it can be used to check if a string contains the specified search pattern
'''

import re # importing regular expression module

txt="the rain in spain"
#search the string that starts with "the" and ends with "spain"
x=re.search("^the.*spain$",txt)


'''
meta-characters: are the characters with special meaning:
[]         A set of characters	                                                                 "[a-m]"	
\       	Signals a special sequence (can also be used to escape special characters)	         "\d"	
.       	Any character (except newline character)	                                         "he..o"	
^       	Starts with	                                                                         "^hello"	
$       	Ends with	                                                                         "planet$"	
*       	Zero or more occurrences	                                                         "he.*o"	
+       	One or more occurrences	                                                             "he.+o"	
?       	Zero or one occurrences	                                                             "he.?o"	
{}       	Exactly the specified number of occurrences	                                         "he.{2}o"	
|       	Either or	                                                                         "falls|stays"	
()       	Capture and group	 
'''


'''
RegEx methods

findall(): returns a list containing all matches
search(): returns a match object if there is a match anywhere in the string
split(): returns a list where the string has been split at each match
sub(): replaces one or many matches with a string

'''

txt="helllllo my name lala is la jyoti lalala jain"
x=re.search("help*.",txt) #op: hell
print(x)
x=re.search("hel*.",txt)
print(x) # helllllo

x=re.findall('la',txt)
print(x) # [la,la,la,la,la,la]

x=re.split('la',txt,1) # will split the txt at first la
print(x) #op:

x=re.sub('la','ha',txt) # will replace all la with ha
print(x) #op: helllllo my name haha is ha jyoti hahaha jain


# there are many meta character in this module you can read about them more at w3school

'''
 match object is an object containing information about search and the result
if there is no match, the value "None" will be returned , instead of match object

match oject properties and methods:

.span(): returns a tuple conatining the start and end postion of the match

.string : returns the string passed into the function

.group(): returns the part of the string where there was a match
'''

txt="the rain is insane"
x=re.search('ai',txt)

tuple1=x.span()
for i in tuple1:
    print(i)

print(txt[5:7])
print(len(txt))

print(x.string) # op: the rain is insane

print(x.group()) # 
