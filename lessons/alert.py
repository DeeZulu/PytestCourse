from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils import calc

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    browser.switch_to.alert.accept()
    value = calc(int(browser.find_element(By.XPATH, "//span[@id='input_value']").text))
    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(value)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
finally:
    sleep(10)
    browser.quit()
