#REGEX sub() method, find and replace
#Where as compile was just find

import re
name=re.compile(r'Agent \w+')
mo=name.findall('Agent Bir gave documents to Agent Anmol')
print(mo)
mo=name.sub('XXXYYYZZZ','Agent Bir gave documents to Agent Anmol')
print(mo)

name=re.compile(r'Agent (\w)\w+')
mo=name.findall('Agent Bir gave documents to Agent Anmol')
print(mo)
mo=name.sub(r'Joker \1 ****','Agent Bir gave documents to Agent Anmol')
print(mo)
#\1 indicates use data of group 1

#VERBOSE REGULAR EXPRESSION

pno=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
pno1=re.compile(r'''
\d\d\d  #Area Code
-   #first dash
\d\d\d #3 digits
-     #second dash
\d\d\d\d   #number
''',re.VERBOSE) # allows to add comments and documentation to the regex pattern
mo=pno.findall('123-234-3456')
mo2=pno.findall('123-234-3456')
print(mo)
print(mo2)
# PASSING MANY OPTIONS
# re.compile(r'',re.ann|re.bb|re.ccc)
