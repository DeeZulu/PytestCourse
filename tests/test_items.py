from selenium.webdriver.common.by import By


def test_cart(browser):
    link = 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
    browser.get(link)
    assert browser.find_element(By.XPATH, "//button[@value='Add to basket']"), "кнопка 'Добавить в корзину отсутствует'"

