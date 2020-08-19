#Selenium and lastest ChromeDriver must be installed
#Configure the bat file to run with command line
from selenium import webdriver
import time
import secrets
#Do make necessary changes in secrets.py
class onlineClass:
    def __init__(self):
        self.oncall=False
        self.loggedin=False
        self.onceloggedin=False
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--disable-notifications')
        self.options.add_experimental_option("prefs", { \
            "profile.default_content_setting_values.media_stream_mic": 2, 
            "profile.default_content_setting_values.media_stream_camera": 2,
            "profile.default_content_setting_values.geolocation": 1, 
            "profile.default_content_setting_values.notifications": 2
          })
        self.browser=webdriver.Chrome(options=self.options)
        self.browser.maximize_window()
    def loadGoogle(self):
        try:
            self.browser.get('https://www.google.co.in/')
            time.sleep(2)
        except:
            self.browser.refresh()
    def login(self):
        try:
            if self.loggedin:
                return
            self.loadGoogle()
            elem=self.browser.find_element_by_id('gb_70')
            elem.click()
            time.sleep(4)
            if self.onceloggedin:
                obj=self.browser.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div')
                obj.click()
                time.sleep(4)
            else:
                self.onceloggedin=True
                elem=self.browser.find_element_by_xpath('//*[@id="identifierId"]')
                elem.send_keys(secrets.user)
                but=self.browser.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
                but.click()
                time.sleep(5)
            elem=self.browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
            elem.send_keys(secrets.passw)
            but=self.browser.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
            but.click()
            self.loggedin=True
            time.sleep(2)
        except:
            self.browser.refresh()
    def Call(self,url):
        try:
            if self.oncall==True:
                return
            if not self.loggedin:
                self.login()
            self.oncall=True
            self.browser.get(url)
            time.sleep(2)
            dis=self.browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span')
            dis.click()
            time.sleep(5)
            join=self.browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[3]/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
            join.click()
            time.sleep(20)
        except:
            self.driver.refresh()
    def endCall(self):
        if not self.oncall:
            return
        self.oncall=False
        self.browser.refresh()
        time.sleep(10)
    def logout(self):
        try:
            if not self.loggedin:
                return
            self.loadGoogle()
            but=self.browser.find_element_by_xpath('//*[@id="gbw"]/div/div/div[2]/div[2]/div[1]/a/span')
            but.click()
            time.sleep(2)
            self.browser.find_element_by_xpath('//*[@id="gb_71"]').click()
            self.loggedin=False
        except:
            self.browser.refresh()
    def Close(self):
        self.logout()
        self.browser.quit()

def control(robo):
    day=time.strftime('%a')
    import re
    pat=re.compile(r'(\d{1,2}):(\d{1,2}):(\d{1,2})')
    mo=pat.findall(time.strftime('%H:%M:%S'))
    hrs=mo[0][0]
    mint=mo[0][1]
    sec=mo[0][2]
    if day=='Mon' or day=='Wed' or day == 'Fri':
        print('Present')
        while True:
            
            mo=pat.findall(time.strftime('%H:%M:%S'))
            hrs=mo[0][0]
            mint=mo[0][1]
            sec=mo[0][2]
            if day=='Mon' and int(hrs)==7 and int(mint)==55 and int(sec)<=30:
                robo.Call('https://meet.google.com/vyc-fpgr-xma')#Mup tut
            elif int(hrs)==8 and int(mint)==55 and int(sec)<=30:
                robo.Call('https://meet.google.com/zoh-jhmv-fts') #DSA
            elif int(hrs)==9 and int(mint)==55 and int(sec)<=30:
                robo.endCall()
            elif int(hrs)==15 and int(mint)==55 and int(sec)<=30:
                robo.Call('https://meet.google.com/jqo-ztvd-xot') #GITA
            elif int(hrs)==16 and int(mint)==55 and int(sec)<=30:
                robo.endCall()
                robo.Call('https://meet.google.com/oxm-piga-mua') #EVS
            elif int(hrs)==17 and int(mint)==55 and int(sec)<=10:
                robo.endCall()
                break
            elif int(hrs)>=18:
                break
    elif day=='Tue' or day=='Thu' or day == 'Sat':
        while True:
            mo=pat.findall(time.strftime('%H:%M:%S'))
            hrs=mo[0][0]
            mint=mo[0][1]
            sec=mo[0][2]
            if int(hrs)==8 and int(mint)==55 and int(sec)<=30:
                robo.Call('http://meet.google.com/fbv-aymg-ggj') #DBS
            elif int(hrs)==9 and int(mint)==55 and int(sec)<=30:
                robo.endCall()
                robo.Call('https://meet.google.com/rsf-fywc-iwq') #MuP
            elif int(hrs)==10 and int(mint)==55 and int(sec)<=30:
                robo.endCall()
                robo.Call('https://meet.google.com/vov-noej-kaw?hs=122&authuser=1') #POE
            elif int(hrs)==11 and int(mint)==55 and int(sec)<=30:
                robo.endCall()
                robo.Call('https://meet.google.com/imq-cwtr-xcu') #Genetics
            elif int(hrs)==13 and int(mint)==00 and int(sec)<=10:
                robo.endCall()
                break
            elif int(hrs)>=13:
                break
    else:
        while True:
            mo=pat.findall(time.strftime('%H:%M:%S'))
            hrs=mo[0][0]
            mint=mo[0][1]
            sec=mo[0][2]
            if int(hrs)==15 and int(mint)==55 and int(sec)<=30:
                robo.Call('https://meet.google.com/eai-vyqx-pmx') #DBS
            elif int(hrs)==17 and int(mint)==00 and int(sec)<=10:
                robo.endCall()
                break
            elif int(hrs)>=17:
                break
    print('BYE! DONE FOR THE DAY')
    robo.Close()

robo=onlineClass()
control(robo)

