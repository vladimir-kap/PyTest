import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://moitane.ge/shop/5-gudvili/43-axali-xorci-da-xorcproduqti")
time.sleep(3)
el = driver.find_element(By.XPATH, "//div[@class='style__ShopProductSubCategoryChip-sc-1bc3ssb-2 iKSeHs']")
el.click()
time.sleep(3)
driver.quit()