
from selenium import webdriver

browser = webdriver.Chrome("C:\\Chromedriver\\chromedriver")
# webdriver will be find all elements for 5 minutes!
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text