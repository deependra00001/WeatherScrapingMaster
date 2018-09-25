#v_folder_A_queries="C:/Users/dsingh097/Desktop/WA/Python/WeatherScrapingMaster/"
import requests
from bs4 import BeautifulSoup
import urllib, os, urllib.request
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import datetime

file = open(os.path.expanduser(r"~/Desktop/US Weather Data.csv"), "wb")
file.write(
        b"ZipCode,Date,Max Temperature,Min Temperature,Mean Temperature" + b"\n")

Filed_Header="ZipCode,Date,Max Temperature,Min Temperature,Mean Temperature"
print(Filed_Header)

vZipCodeList=["10024" ,"06880"]
vYearList=["2018","2017"]
vMonthList="8"
vDayList=["28","29"]

for vZipCode in vZipCodeList:
	for vYear in vYearList:
		for vMonth in vMonthList:
			for vDay in vDayList:
				vDate=str(vYear)+'-'+str(vMonth)+'-'+str(vDay)
				#url='https://www.wunderground.com/history/monthly/KNYC/date/2018-8?reqdb.zip=10024'
				#url='https://www.wunderground.com/history/daily/KNYC/date/2018-8-28?reqdb.zip=10024'
				url='https://www.wunderground.com/history/daily/KNYC/date/'+vDate+'?reqdb.zip='+str(vZipCode)
				Max_Temp=0
				Min_Temp=0
				Mean_Temp=0
				
				options = webdriver.ChromeOptions()
				options.add_argument('--ignore-certificate-errors')
				options.add_argument('--ignore-ssl-errors')
				
				driver = webdriver.Chrome()
				driver = webdriver.Chrome(chrome_options=options)
				time.sleep(5)
				driver.get(url)
				time.sleep(5)
				html = driver.execute_script("return document.documentElement.outerHTML")
				time.sleep(5)
				sel_soup = BeautifulSoup(html,'html.parser')
				driver.close()
				Max_Temp=sel_soup.find_all("tr")[1].find_all("td")[0].text
				Min_Temp=sel_soup.find_all("tr")[2].find_all("td")[0].text
				Mean_Temp=sel_soup.find_all("tr")[3].find_all("td")[0].text
				CompleteString='"'+str(vZipCode)+'"' +","+ str(vDate) +","+ str(Max_Temp) +","+ str(Min_Temp) +","+ str(Mean_Temp)+ "\n"
				file.write(bytes(CompleteString, encoding="ascii", errors='ignore'))
				#printing to help with any debugging and tracking progress
				print(CompleteString)

file.close()
driver.quit()


