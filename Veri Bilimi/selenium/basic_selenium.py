from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)
time.sleep(2)

driver.maximize_window() #açılan pencereyi tam ekran yapar.
#driver.save_screenshot("github-homepage.png") #açılan pencerenin ekran görüntüsünü alır.

url = "https://github.com/emredmr7"
driver.get(url)

print(driver.title)
if "emredmr7" in driver.title:
    driver.save_screenshot("github-emre.png")

time.sleep(2)
driver.back()
time.sleep(2)
driver.close()