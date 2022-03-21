from selenium import webdriver
import math
import time

def calc(t):
    return str(math.log(abs(12*math.sin(int(t)))))

link ="http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_class_name("btn").click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_tag_name("button").click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла