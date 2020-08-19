#Text files
f=open('abc.txt') #read mode by default
data=f.read() # reads entire data as one string
data2=f.readlines() # list of lines
f.close()
f=open('abc.txt','w') #write mode or use 'a' instead of 'w' to append
f.write('Testing testing testing.......')
f.write('1234....1234444')
f.close()
# TO STORE EVERYTHING AS A DATABASE or Dictionary 
import shelve
sf=shelve.open('test_data')
sf['Cats']=['a','b','c']
sf.close()

sf=shelve.open('test_data')
print(sf['Cats'])
sf.close()
