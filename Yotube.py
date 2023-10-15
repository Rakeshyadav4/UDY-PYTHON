import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=options,service=service_obj)
#driver.get("https://www.youtube.com/")
##driver.refresh()
#driver.maximize_window()
#driver.minimize_window()
#driver.get('https://www.youtube.com/results?search_query=shiloh+and+bros')
#driver.get('https://www.youtube.com/watch?v=MsXdUtlDVhk')
#driver.get('https://youtu.be/MsXdUtlDVhk?t=72')
driver.get('https://www.youtube.com/watch?v=MsXdUtlDVhk')

#driver.maximize_window()
driver.find_element(By.XPATH, '//button[@data-title-no-tooltip="Play"]').click()
driver.find_element(By.XPATH, '//button[@data-title-no-tooltip="Full screen"]').click()
time.sleep(2)
#driver.get('https://youtu.be/EiS5jXQ8oio?t=8') # if you want to start in particular time then pass the video and copy video URL at current time and paste it here.
##driver.find_element(By.XPATH, '//button[@data-title-no-tooltip="Play"]').click()
driver.maximize_window()
#driver.find_element(By.XPATH, '//button[@data-title-no-tooltip="Play"]').click()
#driver.find_element(By.XPATH, '//button[@data-title-no-tooltip="Full screen"]').click()
#time.sleep(6)
#driver.get('https://youtu.be/EiS5jXQ8oio?t=9')
#driver.find_element(By.XPATH, '//button[@data-title-no-tooltip="Play"]').click()
#time.sleep(8)
driver.get('https://youtu.be/ir12Boxh__Q?t=10')
time.sleep(26)
driver.get('https://youtu.be/7xUXnI7Wt4k?t=19')















