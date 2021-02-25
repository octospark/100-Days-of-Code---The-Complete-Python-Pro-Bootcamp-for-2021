from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time


CHROME_WEBDRIVER_PATH = 'C:/Development/chromedriver.exe'
FORM_LINK = 'https://docs.google.com/forms/d/' \
            'e/1FAIpQLScG60feZvT2NU6m4mALR5UjmqNsX427rn4Ntwop6WR2lvsFtA/viewform?usp=sf_link'
SCRAPING_LINK = 'https://www.zillow.com/homes/for_rent/1-_beds/' \
                '?searchQueryState=%7B"pagination"%3A%7B%7D%2C"mapBounds"%3A%7B"west"%3A-' \
                '122.63108290625%2C"east"%3A-122.23557509375%2C"south"%3A37.63322934153811%2C"north' \
                '"%3A37.91708111010459%7D%2C"mapZoom"%3A11%2C"isMapVisible"%3Afalse%2C"filterState"%3A%7B"' \
                'price"%3A%7B"max"%3A872627%7D%2C"beds"%3A%7B"min"%3A1%7D%2C"pmf"%3A%7B"value"%3Afalse%7D%2C"' \
                'fore"%3A%7B"value"%3Afalse%7D%2C"mp"%3A%7B"max"%3A3000%7D%2C"auc"%3A%7B"value"%3Afalse%7D%2C"nc' \
                '"%3A%7B"value"%3Afalse%7D%2C"fr"%3A%7B"value"%3Atrue%7D%2C"fsbo"%3A%7B"value"%3Afalse%7D%2C"cmsn' \
                '"%3A%7B"value"%3Afalse%7D%2C"pf"%3A%7B"value"%3Afalse%7D%2C"fsba"%3A%7B"value"%3Afalse%7D%7D%2C"' \
                'isListVisible"%3Atrue%7D'

BASE_LINK = 'https://www.zillow.com'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 OPR/74.0.3911.107",
    "Accept-Language": "en-US,en;q=0.9",

}


# Get the data from the sraping link
response = requests.get(SCRAPING_LINK, headers=headers)
response.raise_for_status()


soup = BeautifulSoup(response.text, 'html.parser')

properties_prices_soup = soup.select(selector=".list-card-price")
properties_prices = [price.text.split(' ')[0][:6] for price in properties_prices_soup]

properties_links_soup = soup.select(selector='article div.list-card-top a')
properties_links = []
for link in properties_links_soup:
    if BASE_LINK not in link['href']:
        properties_links.append(BASE_LINK + link['href'])
    else:
        properties_links.append(link['href'])

properties_address_soup = soup.select(selector='.list-card-addr')
properties_address = [addr.text for addr in properties_address_soup]


# Complete the forms with the data
driver = webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH)


def get_input_path(n):
    return f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{n}]/div/div/div[2]/div/div[1]/div/div[1]/input'


for i in range(len(properties_prices)):
    driver.get(FORM_LINK)
    time.sleep(1)
    address = driver.find_element_by_xpath(get_input_path(1))
    address.send_keys(properties_address[i])
    price = driver.find_element_by_xpath(get_input_path(2))
    price.send_keys(properties_prices[i])
    link = driver.find_element_by_xpath(get_input_path(3))
    link.send_keys(properties_links[i])
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()
    time.sleep(1)

driver.quit()
