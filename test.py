import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://yandex.ru/")
into = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div/div[1]/div/div/a[1]').click()
login = driver.find_element(by=By.XPATH, value='//*[@id="passp-field-login"]')
login.send_keys('+79786621628')

driver.get("https://yandex.ru/maps")
element = driver.find_element(by=By.TAG_NAME, value="input")
element.send_keys("Rostov")
element.submit()
#element = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[9]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div[2]/span[2]/div/div/div/div[1]')

for element in driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[9]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div[2]/span[2]/div/div/div/div[1]'):
    print(element.text)

time.sleep(5)
driver.close()