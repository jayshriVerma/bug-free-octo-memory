from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver=webdriver.Chrome()
# driver.get("https://www.seleniumhq.org")
# findid=driver.find_element_by_id('q')
# findname=driver.find_element_by_name('q')

# findclass=driver.find_element_by_class_name('selenium-sponsors')
# findxpath=driver.find_element_by_xpath('//*[@id="class-content"]/h1[1]')

# print("My input element is")
# print(findid)
# print(findname)
# print(findclass)
# print(findxpath)
# driver.close()
driver=webdriver.Chrome()
driver.get("https://python.org")
search=driver.find_element_by_name('q')
search.clear()
search.send_keys("pycon")
search.send_keys(Keys.RETURN)
time.sleep(4)
driver.close()
