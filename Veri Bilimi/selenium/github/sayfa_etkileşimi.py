from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys #enter, space gibi tuşları kullanmak için

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)
driver.maximize_window()

seachInput = driver.find_element_by_name("q")
time.sleep(1)
seachInput.send_keys("python")
time.sleep(3)
seachInput.send_keys(Keys.ENTER)
time.sleep(3)

result = driver.find_elements_by_css_selector(".repo-list-item a")
for element in result:
    print(element.text)

driver.close()