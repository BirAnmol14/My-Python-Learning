#REGEX -> regular expressions for pattern matching
#Without Regex
def isPhone(text):
    c1=len(text)
    if c1!=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3]!='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7]!='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    print('found: '+text)
    return True

print(isPhone('Pk'))
print(isPhone('111-222-1234'))
message='call me 444-555-1234, or at 123-234-3456'

found=False
for i in range(len(message)):
    ret=isPhone(message[i:i+12])
    if ret==True:
        found=True
        print(message[i:i+12]+' was found')
if not found:
    print('No number found in the message')

print('*********************')
#MAKE IT SIMPLER USING REGEX
import re
phoneRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #using raw string to find 3digit-3digits-4digits
mo=phoneRegex.search(message)#finds 1st matching object, returns a group object
mo2=phoneRegex.findall(message)#finds all returns a list
print(mo.group())
print(mo2)
print('************************')
#neglecting some elements in the string
x=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') #use brckets for sub grouping 
y=x.search(message)
print(y.group())
print(y.group(3))
#Finding paranthesis

x=re.compile(r'\(\d\d\d-\d\d\d-\d\d\d\d\)')
y=x.search('my number is (999-888-7654)')
print(y.group())
print('*********************************')
#piping
batreg=re.compile(r'bat(man|mobile|copter)') #bat prefix, and others are just suffix
x=batreg.findall('batman has batmobile and a batcopter')
print(x)#returns all matching suffix

