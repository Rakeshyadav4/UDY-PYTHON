from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#chrome driver is a middle man who understand all your script and anaylis and pass the information to chrome browser
#chrome driver - chrome browser
service_obj = Service()  # so this the third man because I cannot talk to browser directly hence created this service
driver = webdriver.Chrome(service=service_obj)  # this driver is responsible to perform all the actions
driver.get("https://www.google.com")
print(driver.title) # how to get the title = Google
print(driver.current_url) # how to see and get whether we are in correct URL = https://www.google.com/
#driver.maximize_window()
driver.get('https://rahulshettyacademy.com/')
#driver.close()  # how to close the browser
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.back()
driver.forward()
driver.refresh()