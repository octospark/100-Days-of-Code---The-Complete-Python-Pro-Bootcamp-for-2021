from selenium import webdriver
import time

chrome_webdriver_path = "C:/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_webdriver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

ids_list = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyMine",
            "buyShipment", "buyAlchemy lab", "buyPortal", "buyTime machine"]
ids_list.reverse()

cookie = driver.find_element_by_id("cookie")
money = int(driver.find_element_by_id("money").text)

start_time = time.time()
while True:
    cookie.click()
    if int(time.time()*10) % 123 == 0:
        money = int(driver.find_element_by_id("money").text.replace(",", ""))
        try:
            for id_name in ids_list:
                str_number = driver.find_element_by_id(id_name).text.split("\n")[0].split("-")[1]
                str_number = str_number.strip()
                upgrade_value = int(str_number.replace(",", ""))
                if money > upgrade_value:
                    driver.find_element_by_id(id_name).click()
                    break
        except:
            pass
    if time.time() - start_time > 300:
        break

print(driver.find_element_by_id("cps").text)

