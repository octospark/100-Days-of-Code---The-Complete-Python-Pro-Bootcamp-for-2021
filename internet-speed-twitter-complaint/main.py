from selenium import webdriver
import time

PROMISED_DOWN = 6
PROMISED_UP = 1
CHROME_DRIVER_PATH = 'C:/Development/chromedriver.exe'
TWITTER_EMAIL = 'ASpeedTester1'
TWITTER_PASSWORD = 'tester123!'


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        go_button = self.driver.find_element_by_class_name("js-start-test")
        go_button.click()
        time.sleep(60)

        results = self.driver.find_elements_by_class_name("result-data-large")
        self.down = float(results[1].text.strip())
        self.up = float(results[2].text.strip())

    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            self.driver.get("https://twitter.com/login")
            time.sleep(10)
            credentials = self.driver.find_elements_by_class_name('r-30o5oe')
            user = credentials[0].send_keys(TWITTER_EMAIL)
            password = credentials[1].send_keys(TWITTER_PASSWORD)
            submit = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/'
                                                       'div/div[3]/div/div/span/span')
            submit.click()
            time.sleep(17)
            content_container = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/'
                                                                  'div/div/div/div[2]/div/div[2]/div[1]/div/div/div/'
                                                                  'div[2]/div[1]/div/div/div/div/div/div/div/div/div/'
                                                                  'div[1]/div/div/div/div[2]/div/div/div/div')
            content_container.send_keys(f'Hey there @vodafone_al my download speed is {self.down} and '
                                        f'upload speed is {self.up}. This is below the terms of our contract of '
                                        f'6Mbs down and 1Mbps up')
            tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
                                                             'div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                             'div[4]/div/div/div[2]/div[3]/div/span/span')
            tweet_button.click()
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
