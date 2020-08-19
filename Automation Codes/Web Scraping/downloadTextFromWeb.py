# Using request module to download stuff from web

import requests
ro=requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(ro.status_code) #404 not found, 200 correct
try:
    ro.raise_for_status() #checks if file downloaded else raise exception
    print(len(ro.text)) #ro.text will contain the entire data
    out=open('romeo&juliet.txt','wb')#write binary data to maintain integrity and encodig
    for chunk in ro.iter_content(100000):
        out.write(chunk)
    out.close()
except:
    print('Error!')

