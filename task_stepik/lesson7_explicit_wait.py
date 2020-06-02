from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    y = math.log(abs(12 * math.sin(x)))
    return str(y)

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome("C:\\Chromedriver\\chromedriver")
browser.get(link)
try:
    book_value = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book_button = browser.find_element_by_id("book")
    book_button.click()
    browser.execute_script("window.scrollBy(0,120);")
    x_elem = browser.find_element_by_id("input_value")
    x = int(x_elem.text)
    y = calc(x)
    text = browser.find_element_by_id("answer")
    text.send_keys(y)
    submit_button = browser.find_element_by_id("solve")
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()

