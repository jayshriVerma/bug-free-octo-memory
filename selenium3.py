from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("file:///C:/Users/Yogesh/Desktop/form.html")
loginform_absolute=driver.find_element_by_xpath("/html/body/form[1]")
loginform_relative=driver.find_element_by_name("//form[1]")

loginform_byid=driver.find_element_by_name("//form[@id='loginForm']")

print("My input element is")
print(loginform_absolute)
print(oginform_relative)
print(loginform_byid)
driver.close()
