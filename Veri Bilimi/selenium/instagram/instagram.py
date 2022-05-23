from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self, username, password):
        self.browser    = webdriver.Chrome()
        self.username   = username
        self.password   = password
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)
        usernameInput   = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput   = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
        
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)
    def skipNotif(self):
        self.browser.get("https://www.instagram.com/accounts/onetap/?next=%2F")
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
        time.sleep(2)
    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)
        
        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followersCount = len(dialog.find_elements_by_css_selector("li"))
        print(f"first count {followersCount}")

        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_down(Keys.SPACE).perform()
            time.sleep(1)

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followersCount != newCount:
                followersCount = newCount
                print(f"second count : {newCount}")
                time.sleep(1)
            else:
                break

        followers = dialog.find_elements_by_css_selector("li")

        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            print(link)
    def followUsers(self, kullaniciAdi):
        self.browser.get("https://www.instagram.com/"+kullaniciAdi)
        time.sleep(2)

        followButton = self.browser.find_element_by_tag_name("button")
        if followButton.text != "Takiptesin":
            followButton.click()
            time.sleep(2)
        else:
            print("Zaten Takiptesin")

insta = Instagram(username, password)
insta.signIn() 
insta.skipNotif()
# insta.getFollowers()
insta.followUsers("atilsamancioglu")