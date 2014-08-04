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
Aug 03 2014    Kyle Dove            Code clean up
Aug 03 2014    Kyle Dove            Added for loop navigating to answers and printing them. It's
                                    using xpath, which is apparently frowned upon in this
                                    establishment, and may or may not work moving forward
'''

from selenium import webdriver
import time

#For Chrome use
#chromeDriverPath = "C:/ChromeBinary/chromedriver.exe"
#driver = webdriver.Chrome(chromeDriverPath)

separator=":"
fileIN = open('creds', "r")
line = fileIN.readline()

qtxt = "qtext_"
atxt = "my_answer_"

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

#Print Source Page for testing purposes
print(driver.page_source)
print('\n \n \n New Page \n \n \n')

time.sleep(5)

#Greg's way of clicking the link
driver.find_element_by_css_selector("#pane_new > div.links > ul > li > a").click()

time.sleep(10)

#Greg's way of clicking the link
driver.find_element_by_css_selector("#questions_intro > div.buttons > ul > li > button").click()

#Greg's way of getting question and printing it
question = driver.find_element_by_css_selector("div[id^="+qtxt+"]").text
print(question)

#Have no fear Simon Belmont is here with the power of Christ infused in my spear
#For loop for navigating and printing answers
for x in range(1, 3):
    x2 = str(x)
    answer = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/div[4]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[3]/form/div[1]/label[" + x2 + "]").text
    print(answer)

#Close Down
#driver.close()