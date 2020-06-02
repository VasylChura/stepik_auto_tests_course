from selenium import webdriver

browser = webdriver.Chrome("C:\\Chromedriver\\chromedriver")
browser.get("http://suninjuly.github.io/cats.html")
b = browser.find_element_by_id("button")