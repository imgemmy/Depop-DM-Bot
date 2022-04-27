from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

driver = webdriver.Chrome('./chromedriver')

driver.get("https://www.depop.com/login/")

usernames_json = open('usernames.txt', 'r+')

#ENTER YOUR FIELDS HERE
profile_username = ""
profile_password = ""
search_item_name = ""
dm_message = ""
#POST # COUNT
countNow = 2

#USER LOGIN VAR
user_login = driver.find_element_by_id("username")
user_password = driver.find_element_by_id("password")

#LOGIN TO ACCOUNT
user_login.clear()
time.sleep(3)
user_login.send_keys(profile_username)
time.sleep(2)
user_password.clear()
user_password.send_keys(profile_password)
user_password.send_keys(Keys.RETURN)
time.sleep(2)





#SEARCH HASHTAGS
search = driver.find_element_by_name("q")
search.clear()
search.send_keys(search_item_name)
search.send_keys(Keys.RETURN)
time.sleep(1)




#BEGIN CLICKING ON FIRST 
def getFirstPost():
    time.sleep(3)
    post_element = driver.find_element_by_xpath('/html/body/div[1]/main/div[3]/div/ul/li['+str(countNow)+']')
    post_element.click()
    time.sleep(2)
getFirstPost() #exectutes clicking on post



#MESSAGE USER
def messageUser():
    message_user_btn = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[3]/div/div[1]/div[2]/a') #CLICKS THE MESSAGE BUTTON FROM PRODUCT PAGE
    message_user_btn.click()
    time.sleep(2)
    message_user_text = driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/div[2]/div/form/textarea') #GETS INPUT ON DM PAGE
    message_user_text.click()
    message_user_text.send_keys(dm_message) #SENDS THE MESSAGE
    time.sleep(1)
    message_user_text.send_keys(Keys.RETURN)
messageUser() #exectutes messaging user


#REPEATING THE PROCCESS

#GO BACK TO SEARCH RESULTS
#driver.back()
#time.sleep(2)
#driver.back()
#time.sleep(2)

#while countNow > 1:
#    driver.back()
#    time.sleep(5)
#    driver.back()
#    time.sleep(5)
#    countNow = countNow + 1
#    getFirstPost()
#    time.sleep(2)
#    messageUser()
#    time.sleep(3)
def scroll_down():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

add_one = 0

while countNow > 1:
    time.sleep(1)
    driver.get('https://www.depop.com/search/?q='+search_item_name)
    time.sleep(2)
    countNow = countNow + 1
    if countNow % 24:
        add_one = add_one + 1
        add_one*scroll_down()
        
    getFirstPost()
    time.sleep(2)
    messageUser()
    




