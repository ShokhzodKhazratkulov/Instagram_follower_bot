from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

INSTA_USERNAME = "Your username"
INSTA_PASSWORD = "password"
TARGET_ACCOUNT = "target account name"
INSTA_URL = "https://www.instagram.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InstaFollower:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(options=driver_path)

    def login(self):
        self.driver.get(INSTA_URL)
        time.sleep(2)
        username = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        username.send_keys(INSTA_USERNAME)
        password.send_keys(INSTA_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        button = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        time.sleep(3)
        button.click()
        time.sleep(5)
        notification_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        time.sleep(3)
        notification_button.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/followers/")
        time.sleep(5)
        bar = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')

        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", bar)
            time.sleep(1)
            bot.follow()
            time.sleep(3)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value="._aano button")

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


bot = InstaFollower(chrome_options)

bot.login()
bot.find_followers()
bot.follow()



