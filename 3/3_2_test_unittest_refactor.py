from selenium import webdriver
import time
import unittest

browser = webdriver.Chrome()

def fields_filler(link):
    browser.get(link)
    # Код, который заполняет обязательные поля
    text = 'Some text'
    browser.find_element_by_css_selector(".first_block input.first").send_keys(text)
    browser.find_element_by_css_selector(".first_block input.second").send_keys(text)
    browser.find_element_by_css_selector(".first_block input.third").send_keys(text)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    # находим и возвращаем элемент, содержащий текст
    return browser.find_element_by_tag_name("h1").text
    
class TestRegistrationForm(unittest.TestCase):
    # Проверка формы без бага
    def test_registration1(self):
        self.assertEqual("Congratulations! You have successfully registered!", \
          fields_filler("http://suninjuly.github.io/registration1.html"), "Registration failed")

    def test_registration2(self):
        self.assertEqual("Congratulations! You have successfully registered!", \
          fields_filler("http://suninjuly.github.io/registration2.html"), "Registration failed")   

if __name__ == "__main__":
    unittest.main()