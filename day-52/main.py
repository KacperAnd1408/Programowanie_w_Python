from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

SIMILAR_ACCOUNT = "chefsteps"
USERNAME = "Let_Him_Cook333"
PASSWORD = "Fangaly12"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url="https://www.instagram.com/accounts/login/")
        self.driver.maximize_window()

    def login(self):
        time.sleep(4)

        cookies = self.driver.find_element(By.XPATH, value='/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        if cookies:
            cookies.click()

        email = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.send_keys(USERNAME)

        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD, Keys.ENTER)

        time.sleep(7)

        # not_now = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        # if not_now:
        #     not_now.click()
        #
        # notific = self.driver.find_element(By.XPATH, value="//button[normalize-space()='Not Now']")
        # if notific:
        #     notific.click()

        time.sleep(10)

    def find_followers(self):
        self.driver.get("https://www.instagram.com/chefsteps/")
        time.sleep(3.5)
        followers = self.driver.find_element(By.CSS_SELECTOR, value="ul li div a[href='/chefsteps/followers/']")
        followers.click()
        time.sleep(2)
        # modal = self.driver.find_element(By.CLASS_NAME, value="xyi19xy")
        # modal = self.driver.find_element(By.XPATH, value="/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        modal = self.driver.find_element(By.CSS_SELECTOR, value=".xyi19xy")
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(3)


    def follow(self):

        accounts = self.driver.find_elements(By.CSS_SELECTOR, value='button . _acan _acap _acas _aj1- _ap30')
        for account in accounts:
            print(account.text)



bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

