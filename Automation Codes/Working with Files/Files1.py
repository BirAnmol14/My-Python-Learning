#Let's learn about files
# use '\\'->for backslash in string or use raw string r'\'
import os
loc=os.path.join('folder1','folder2','folder3','fileabc.txt')
print(loc+'\n'+os.sep)
print(os.getcwd())# By default everything searched and saved in current working directory cwd
# os.chdir() ->to change current working directory
print(os.path.abspath('SeleniumDemo.py'))


total=0
for filename in os.listdir(os.getcwd()):
    if not os.path.isfile(os.path.join(os.getcwd(),filename)):
        continue
    total+=os.path.getsize(os.path.join(os.getcwd(),filename))
print('Total size '+str(total))
