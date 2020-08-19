#Regex advanced
# ? character -> optional my appear once or never
import re
batreg=re.compile(r'bat(wo)?man') #this means the wo group can apperaer 0 or one times in the pattern
mo=batreg.search('Adventures of batman')
print(mo.group())
mo=batreg.search('Adventures of batwoman')
print(mo.group())
mo=batreg.search('Adventures of batwowoman')
if not mo==None: 
    print(mo.group())
else: print('None')
mo=batreg.search('Adventures of batwo')
if not mo==None: 
    print(mo.group())
else: print('None')
print('***************************************')
preg=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=preg.search('My number is 111-222-3333')
if not mo==None:
    print(mo.group())

preg=re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo=preg.search('My number is 222-3333')
if not mo==None:
    print(mo.group())

def aQuestion(str):
    print('***********************************')
    a=re.compile(r'\?')
    mo=a.search(str)
    if mo ==None:
        print('No an interrogative sentence')
        print('***********************************')
        return
    print('How dare you ask me a question')
    print('***********************************')
aQuestion('How are you?')
aQuestion('bye!')

#Like ? (0 or 1) characters
# * matches 0 or more times
batreg=re.compile(r'bat(wo)*man') #this means the wo group can apperaer 0 or one times in the pattern
mo=batreg.search('Adventures of batman')
print(mo.group())
mo=batreg.search('Adventures of batwoman')
print(mo.group())
mo=batreg.search('Adventures of batwowoman')
print(mo.group())
# to match * use \*
#+ matches one or more times
#use \+ to match a plus  in the string


msg='does 2+3-4*8=23? 123+*?'
t=re.compile(r'\+\*\?')
mo=t.findall(msg)
print(mo)

#Exact number of repetitions
laugh=re.compile(r'(ha){3}')#must be consecutive repititions
mo=laugh.search('hahaha he said')
print(mo.group())

pno=re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo=pno.search('my numbers are 999-888-7777,887-7654,123-234-3456')
print(mo.group())


#range of reps
# (){min,max}
#(){min,}->till infy
#(){,max}->0 to max
# by default greedy match, tries to match as many as possible
#to mke non-greedy match, (){}? write this, it will try to match the minimum number of times

