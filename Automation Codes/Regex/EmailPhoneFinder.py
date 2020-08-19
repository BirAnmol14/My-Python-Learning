#! python3
#Shabang line to tell the version of python to run
# Run on any sentence stored on clipboard
import re
import pyperclip

pno=re.compile(r'''
# We can expect numbers like
# 123-234-3456, 123-1234, (123) 123-2345, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?    #area code optional
(\s|-)    #Separator
(\d\d\d)    #next 3 digits
-    #Separator
(\d\d\d\d)    #last 4 digits
(\s(ext(\.)?\s|x)(\d{2,5}))?# extension (optional)
)
''',re.VERBOSE)

email=re.compile('''
#sss@sss.abc
[a-zA-Z0-9_.+]+    #name
@    #@
[a-zA-Z0-9_.+]+   #domain
''',re.VERBOSE)

text=pyperclip.paste()

mpno=pno.findall(text)
emno=email.findall(text)
print('Phone:')
print(mpno)
print('email:')
print(emno)
ph=[]
for num in mpno:
    ph.append(num[0].strip())
print(ph)

phstr='\n'.join(ph)
estr='\n'.join(emno)
print(phstr)
print(estr)

dat='\n\n'.join(['\n\nRESULTS:',phstr,estr])
print(dat)

pyperclip.copy(dat)

'''Data:
ABC     123-234-1234    BIR@XCJO.COM
ASD     (123) 234-4545  ALP@DBSDKNFK.EDI
JKL     123-9090    JOHN.SNOW_KELLY@GMIAL.COM
XCVBNM  098-1234 ext. 12345     kelly90@funda.usa
sdn     123-123-1234 x12345     jell_belly@giglly.edu
nfej    111-2222 ext 12345  gel_bell_@6789.sad
'''
