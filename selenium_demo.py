from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://iknow.jp/courses/566921')

time.sleep(20)

driver.quit()