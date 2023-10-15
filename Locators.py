from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=options,service=service_obj)
driver.get('https://rahulshettyacademy.com/angularpractice/')
# selenium supports the locator to identify the element like ID, Name, CSS selector, Xpath, linkText
driver.find_element(By.NAME, 'email').send_keys('Hello@gmail.com')
driver.find_element(By.ID, 'exampleInputPassword1').send_keys("123456")
driver.find_element(By.ID, 'exampleCheck1').click()
#If you don't have any locator which selenium supports we can use xpath or CSSS Selector
#Syntex for Xpath = //(tagname[@attribute='value'])
#Syntex for CSS Selector = (tagname[attribute='value'])
driver.find_element(By.CSS_SELECTOR, 'input[name= "name"]').send_keys('Rakesh') # to enter name on name tab
driver.find_element(By.XPATH, '//input[@type="submit"]').click() # to click on submit.