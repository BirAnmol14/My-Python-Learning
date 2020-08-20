#My very firt attemp at gui with python
#Covid-19 tracker with tkinter GUI and JSON handling.
#Download requests module
#Data being taken from https://www.coronatracker.com/

import requests
import tkinter as tk
import json
import os


def getCountryDB():
    url='http://api.coronatracker.com/v3/stats/worldometer/country'
    data=requests.get(url)
    data=data.json()
    details=[]
    for info in data:
        details.append({'country':info['country'],'code':info['countryCode']})
    return details

def buildCountryDb():
    countryMapping=[]
    if os.path.isfile(os.getcwd()+'/countryMapping.txt'):
        try:
            file=open('countryMapping.txt','r')
            while True:
                line=file.readline()
                if not line:
                    break
                countryMapping.append(json.loads(line))
        finally:
            file.close()
    else:
        try:
            file=open('countryMapping.txt','w')
            countryMapping=getCountryDB()
            for country in countryMapping:
                file.write(json.dumps(country)+'\n')
        finally:
            file.close()
    return countryMapping 

def countrySpecificInfo(countryCode):
    data=requests.get('https://api.coronatracker.com/v3/stats/worldometer/country?countryCode='+countryCode)
    return data.json()

def prettyPrint(countryCode):
    info=countrySpecificInfo(countryCode)[0]
    string=''
    string+='Total Confirmed Cases: '+"{:,}".format(info['totalConfirmed'])+'\n'
    string+='Total Deaths: '+"{:,}".format(info['totalDeaths'])+'\n'
    string+='Total Recovered Cases: '+"{:,}".format(info['totalRecovered'])+'\n'
    string+='Active Cases: '+"{:,}".format(info['activeCases'])+'\n'
    string+='Daily Confirmed Cases: '+"{:,}".format(info['dailyConfirmed'])+'\n'
    string+='Daily Deaths: '+"{:,}".format(info['dailyDeaths'])+'\n'
    detailed=''
    for key in info:
        detailed+=key+': '+str(info[key])+'\n'
    return (string,detailed)

countryMapping=buildCountryDb()

def getCountry():
    if len(txt.get())==0:
        return
    country=txt.get()
    txt.delete(0,len(country))
    txt.pack_forget()
    getBut.pack_forget()
    getList.pack_forget()
    id=-1
    for countries in countryMapping:
        if country.lower()==countries['country'].lower():
            id=countries['code']
            break
    resetBut.pack(padx=10, pady=10)
    if id==-1:
        dataLabel.configure(text='Country Not Found')
        details.configure(text=' ')
        details.pack(padx=10, pady=10)
    else:
        dataLabel.configure(text=country.upper()+' ('+id+')')
        tuple=prettyPrint(id)
        details.configure(text=tuple[0])
        extraDetails.configure(text=tuple[1])
        details.pack(padx=10, pady=10)
        extraInfo.pack(padx=10, pady=10)
    

def reset():
   dataLabel.configure(text='Enter country name')
   details.pack_forget()
   extraDetails.pack_forget()
   resetBut.pack_forget()
   extraInfo.pack_forget()
   lessInfo.pack_forget()
   txt.pack(padx=10, pady=10)
   getBut.pack(padx=10, pady=10)
   getList.pack(padx=10, pady=10)

def getDetailed():
    extraDetails.pack(padx=10, pady=10)
    details.pack_forget()
    extraInfo.pack_forget()
    lessInfo.pack(padx=10, pady=10)
    
def getSimple():
    details.pack(padx=10, pady=10)
    extraDetails.pack_forget()
    extraInfo.pack(padx=10, pady=10)
    lessInfo.pack_forget()

def getCountryList():
    newWindow=tk.Toplevel(root)
    newWindow.title('Corona Data Tracker')
    newWindow.geometry('200x200')
    listbox = tk.Listbox(newWindow,selectmode='single')
    def curSelect(event):
        widget = event.widget
        selection=widget.get('anchor')
        txt.delete(0,len(txt.get()))
        txt.insert('end',selection)
        newWindow.destroy()
        getBut.invoke()
    listbox.bind('<<ListboxSelect>>',curSelect)
    listbox.pack() 
    scrollbar = tk.Scrollbar(newWindow) 
    #scrollbar.pack(side = 'right', fill = 'both')
    list=[]
    for country in countryMapping:
        list.append(country['country'])
    list.sort()
    for country in list:
        listbox.insert('end', country) 
    listbox.config(yscrollcommand = scrollbar.set) 
    scrollbar.config(command = listbox.yview)


#Building UI
root=tk.Tk()
root.geometry('700x600')
root.title('Corona Data Tracker')
dataLabel=tk.Label(root,text='Enter country name',font=('poppins',20,'bold'))
txt=tk.Entry(root,width=50)
getBut=tk.Button(root,text='Get Data',command=getCountry)
getList=tk.Button(root,text='Get List of Countries',command=getCountryList)
dataLabel.pack(padx=10, pady=10)
txt.pack(padx=10, pady=10)
getBut.pack(padx=10, pady=10)
getList.pack(padx=10, pady=10)
details=tk.Label(root,font=('poppins',14))
extraDetails=tk.Label(root,font=('poppins',14))
lessInfo=tk.Button(root,text='Simple Information',command=getSimple)
extraInfo=tk.Button(root,text='Detailed Information',command=getDetailed)
resetBut=tk.Button(root,text='Reset',command=reset)
root.mainloop()
