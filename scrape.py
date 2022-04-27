
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path=r"J:\DEPOP DM BOT\chromedriver.exe")

browser.get('https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/')


i = 10

while True:
    agents = browser.find_element_by_xpath('/html/body/div[1]/section[2]/div/div/table/tbody/tr['+str(i)+']/td[1]/a')
    i = i + 1
    print(agents)
