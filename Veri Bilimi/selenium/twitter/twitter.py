from twitterUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self, username, password):
        self.browser    = webdriver.Chrome()
        self.username   = username
        self.password   = password

    def signIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(2)

        usernameInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
        
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def getProfile(self):
        self.browser.get(f"https://twitter.com/{self.username}")

    def search(self, word):
        searchInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
        searchInput.send_keys(word)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(4)

        liste = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]")
        for items in liste:
            print(" ")
            print(items.text)


twit = Twitter(username, password)
twit.signIn()
# twit.getProfile()
twit.search("python")