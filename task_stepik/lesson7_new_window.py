from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome("C:\\Chromedriver\\chromedriver")
browser.get(link)
def calc(x):
    y = math.log(abs(12 * math.sin(x)))
    return str(y)

try:
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    second_win = browser.window_handles[1]
    browser.switch_to.window(second_win)
    x = browser.find_element_by_id("input_value")
    x = int(x.text)
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    submit_button = browser.find_element_by_css_selector("[type='submit']")
    submit_button.click()
    time.sleep(5)
finally:
    time.sleep(5)
    browser.quit()


