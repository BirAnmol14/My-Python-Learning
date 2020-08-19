import re
pno=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=pno.findall('My numbers are 123-234-3456,123-234-5678 and 999-888-7654')
print(mo)
pno=re.compile(r'((\d\d\d)-(\d\d\d)-(\d\d\d\d))')
mo=pno.findall('My numbers are 123-234-3456,123-234-5678 and 999-888-7654')
print(mo)


#\d is a decimal digit
# | piping can be used as OR

#\D-> non numeric

#OWN CHARACTER CLASS

vowel=re.compile(r'[aeiouAEIOU]')#equal to r'a|e|i|o|u|A...'
mo=vowel.findall('Hello Apple')
print(mo)
# to give multiplicity []{num}
#To make a negative character class use ^ ex: [^]
#findall not matching characters
##################################################################
#ex begins with
pat=re.compile(r'^Hello')
mo=pat.search('Hello Bir!')
def test():
    if mo !=None:
        print(mo.group())
    else:
        print('Not found')
test()
mo=pat.search('Bir Hello')
test()

#Checking ending use $
pat=re.compile(r'world$')
mo=pat.search('Hello world')#found
test()
mo=pat.search('Hello world!')#returns None
test()

# all digits r'^\d+$' starts with a digit and has one or more digits and ends with only digits

#. character wild card
# This stands for any character except new line like _ in SQL

pat=re.compile(r'.at')
mo=pat.findall('cat under the mat, was wearing a hat and ate a rat.')
print(mo)


sent='First name: Bir Last Name: Anmol'
name=re.compile(r'First name: (.*) Last Name: (.*)')
mo=name.findall(sent)
print(mo)
#by default greedy, to make non-greedy use .*?

# There are other things you can pass to recompile like
#r'',re.DOTALL matches all .* even if separated by \n, matches new lines as well

# for ignoring case you can pass re.I

