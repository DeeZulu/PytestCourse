import os.path
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils import calc

# browser = webdriver.Chrome()
# browser.execute_script("document.title='Script executing';alert('Robots at work')")
# sleep(10)

#

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    browser.find_element(By.XPATH, "//input[@name='firstname']").send_keys("hui")
    browser.find_element(By.XPATH, "//input[@name='lastname']").send_keys("morzhov")
    browser.find_element(By.XPATH, "//input[@name='email']").send_keys("aga@tam.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test-file.txt')
    browser.find_element(By.XPATH, "//input[@id='file']").send_keys(file_path)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
finally:
    sleep(10)
    browser.quit()
