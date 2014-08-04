'''
Created on Jul 28, 2014

@author: Greg Saxton
@author: Kyle Dove

Purpose: Log in to OKCupid account and cycle through questions.

Modification History:

DATE           Author               Description   
===========    ===============      =============
Jul 28 2014    Kyle Dove            Created
Jul 29 2014    Kyle Dove            Removed credentials from hardcode and placed in separate file
                                    Added logic to advance to the questions page (past the modal 
                                    and past the questions link, to grandmother's house we go)
Aug 03 2014    Kyle Dove            Developed technique to pull question from page source using
                                    regex
Aug 03 2014    Greg Saxton          Developed better technique to pull question from page source
                                    using CSS Selector
'''

from selenium import webdriver
import time
import re


#chromeDriverPath = "C:/ChromeBinary/chromedriver.exe"
#driver = webdriver.Chrome(chromeDriverPath)

separator=":"
fileIN = open('creds', "r")
line = fileIN.readline()

qtxt = "qtext_"

#Working... kind of...
#Don't fucking touch this...
#regex = '<div class="qtext" id="qtext_(.*)>\s<p>(.+?)<\/p>\s<\/div>'
#pattern = re.compile(regex)

#Working... kind of...
#Don't fucking touch this...
#regex = '<div class="qtext" id="qtext_(.*)>\s<p>(.+?)<\/p>\s<\/div>'
#pattern = re.compile(regex)

#Working... kind of...
#Don't fucking touch this...
regex = '<div class="qtext" id="qtext_(.*.)>\s<p>(.+?)<\/p>\s<\/div>'
pattern = re.compile(regex)

while line:
    sout=line.split(separator)
    user=sout[0]
    passwd=sout[1]
    line = fileIN.readline()

print(user)
print(passwd)

driver = webdriver.Firefox()

#Open up web browser at OKCupid page
driver.get('https://www.okcupid.com/')

#Click open sign in button
driver.find_element_by_id("open_sign_in_button").click()

#Find Username and Password Elements by Id
UsernameElement = driver.find_element_by_id("login_username")
PasswordElement = driver.find_element_by_id("login_password")

#Populate Username and Password fields
UsernameElement.send_keys(user)
PasswordElement.send_keys(passwd)

#Click sign in button / submit form
driver.find_element_by_id("sign_in_button").click()

#Print Source Page
print(driver.page_source)

print('\n \n \n New Page \n \n \n')

print(driver.page_source)

print('\n \n \n New Page \n \n \n')

time.sleep(10)

#Fucking Please!!! Why Mega Man X is so fucking good that it makes my dick rock hard
#Click the link to questions
#driver.find_element_by_xpath("//div[@id='main_content']/div[2]/div[1]/ul[1]/li[3]/a").click()

#Greg's way of clicking the link
driver.find_element_by_css_selector("#pane_new > div.links > ul > li > a").click()

time.sleep(10)

#Ridin' on Cars!!!
#Click the accept button on the modal to advance to the questions page
#driver.find_element_by_xpath("//div[@id='questions_intro']/a[1]").click()

#Greg's way of clicking the link
driver.find_element_by_css_selector("#questions_intro > div.buttons > ul > li > button").click()

print(driver.find_element_by_xpath("//div[@id='new_question']"))

print driver.page_source

question = re.search(pattern,driver.page_source)
print(question)

question = re.findall(pattern,driver.page_source)
print(question)

#Greg's way of getting question and printing it
question = driver.find_element_by_css_selector("div[id^="+qtxt+"]").text
print(question)

#Close Down
#driver.close()
