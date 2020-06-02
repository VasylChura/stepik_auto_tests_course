from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome("C:\\Chromedriver\\chromedriver")
browser.get(link)
def calc(x):
    y = math.log(abs(12 * math.sin(x)))
    return str(y)
try:
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)
    send_answer = browser.find_element_by_id("answer")
    send_answer.send_keys(y)
    browser.execute_script("window.scrollBy(0, 120);")
    check_box = browser.find_element_by_id("robotCheckbox")
    check_box.click()
    radio = browser.find_element_by_css_selector("[for='robotsRule']")
    radio.click()
    submit = browser.find_element_by_css_selector("[type = 'submit']")
    submit.click()
    time.sleep(5)

finally:
    time.sleep(5)
    browser.quit()


