from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.XPATH, "//span[@id='num1']").text
    num2 = browser.find_element(By.XPATH, "//span[@id='num2']").text
    value = int(num1) + int(num2)
    li = Select(browser.find_element(By.XPATH, "//select[@id='dropdown']"))
    li.select_by_value(str(value))
    submit = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit.click()

finally:
    sleep(10)
    browser.quit()
