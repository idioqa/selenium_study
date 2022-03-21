import time
from selenium import webdriver
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    with open('test1.txt', 'w') as file:
        file.write('test1 for mls 228')
    path = os.getcwd() + '/' + file.name
    
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element_by_name("firstname").send_keys("Vadym")
    browser.find_element_by_name("lastname").send_keys("T")
    browser.find_element_by_name("email").send_keys("a@a.ru")
    browser.find_element_by_id("file").send_keys(path)
    button = browser.find_element_by_class_name("btn").click()
        
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    #удаляем временный файл
    os.remove(path)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла