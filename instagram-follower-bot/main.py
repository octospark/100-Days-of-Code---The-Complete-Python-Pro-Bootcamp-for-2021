from selenium import webdriver
import time
import random

CHROME_WEBDRIVER_PATH = 'C:/Development/chromedriver.exe'
SIMILAR_ACCOUNTS = ['maniaket_e_librit', 'thenie_shkrime_madheshtore', 'zgjohu1']
USERNAME = 'mendoj_pra_jam'
PASSWORD = 'tetralog'


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USERNAME)
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        log_in = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        log_in.click()
        time.sleep(6)
        save_login_info = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/'
                                                            'main/div/div/div/div/button')
        save_login_info.click()
        time.sleep(3)
        turn_on_notifications = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/'
                                                                  'div/div[3]/button[2]')
        turn_on_notifications.click()

    def find_followers(self):
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNTS[2]}')
        time.sleep(3)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/'
                                                      'header/section/ul/li[2]/a')
        followers.click()
        time.sleep(3)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

        for i in range(20):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        list_of_followers = self.driver.find_elements_by_class_name('sqdOP')

        for person in list_of_followers:
            follow_or_not = random.randint(0, 1)
            if follow_or_not == 1:
                try:
                    time.sleep(2)
                    person.click()
                except:
                    time.sleep(1)
                    cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/'
                                                                      'div/div/div[3]/button[2]')
                    time.sleep(1)
                    cancel_button.click()


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
