from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.get("file:///C:/Users/Yogesh/Desktop/form.html")
select=Select(driver.find_element_by_name('numSelectReturn'))
select.select_by_index(4)
time.sleep(2)
select.select_by_value("250")
time.sleep(2)
select.select_by_visible_text("5000")
time.sleep(2)
options=select.options
print(options)
submit_button=driver.find_element_by_name('continue')
submit_button.submit()
driver.close()