# WEB SCRAPING
#Open a copied webaddress
#! python3
#Must have pyperclip installed
#Can be run with wfind cmd line argument if wfind.bat is configured
import sys
import webbrowser
'''
webbrowser.open('https://google.com')
#Webbrowser can only open
'''

import pyperclip
#Pyperclip helps to open URL copied right before running program
if len(sys.argv)==1:
    add=pyperclip.paste()
    webbrowser.open(add)
else:
    webbrowser.open(sys.argv[1])
#You can also run with system arguments

#www.instagram.com
#Copy url and try