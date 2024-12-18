import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils import calc

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element(By.XPATH, "//input[@id='answer']")
    answer.send_keys(y)
    chkbx = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    chkbx.click()
    rule = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    rule.click()
    submit = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()


