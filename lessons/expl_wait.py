from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from utils import calc

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    WebDriverWait(browser, 10).until(ec.text_to_be_present_in_element((By.ID, "price"), '100'))
    browser.find_element(By.XPATH, "//button[@id='book']").click()
    answer = calc(int(browser.find_element(By.XPATH, "//span[@id='input_value']").text))
    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(answer)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    sleep(10)
    browser.quit()
