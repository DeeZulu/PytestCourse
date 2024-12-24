import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestReg(unittest.TestCase):

    def test_reg_1(self):
        url = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(url)

        f_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        f_name.send_keys("Tom")
        l_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        l_name.send_keys("Soyer")
        email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        email.send_keys("abc@mail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_reg_2(self):
        url = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(url)

        f_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        f_name.send_keys("Tom")
        l_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        l_name.send_keys("Soyer")
        email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        email.send_keys("abc@mail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()
