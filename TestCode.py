__author__ = 'gsaxton'
#import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#chromeDriverPath = "/Users/gsaxton/Downloads/chromedriver_win32"
chromeDriverPath = "C:/ChromeBinary/chromedriver.exe"
#os.environ["webdriver.chrome.driver"] = chromeDriverPath
driver = webdriver.Chrome(chromeDriverPath)

# chromeOpt = webdriver.ChromeOptions._binary_location = os.path.dirname(chromeDriverPath)
driver.get("https://www.okcupid.com/")
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
driver.find_element_by_id("open_sign_in_button").click()
UsernameElement = driver.find_element_by_id("login_username")
PasswordElement = driver.find_element_by_id("login_password")

UsernameElement.send_keys("sdgregorysaxton@gmail.com")
PasswordElement.send_keys("admin1")
driver.find_element_by_id("sign_in_button").click()
time.sleep(5)
driver.find_element_by_css_selector("#pane_new > div.links > ul > li > a").click()
time.sleep(5)
driver.find_element_by_css_selector("#questions_intro > div.buttons > ul > li > button").click()
txt = "qtext_"
otherthing = driver.find_element_by_css_selector("div[id^="+txt+"]").text
print(otherthing)
##qtext_35 > p  #answer_35 > div.container.my_answer > label:nth-child(2)

print("this is a test")


#elem.send_keys("selenium")
#elem.send_keys(Keys.RETURN)
#print(driver.page_source)
#driver.close()


