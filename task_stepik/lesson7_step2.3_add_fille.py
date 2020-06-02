from selenium import webdriver
import time
import os

with open('file.txt', 'w') as file:
   file.write('Hello, World')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome("C:\\Chromedriver\\chromedriver")
browser.get(link)

try:
    input1 = browser.find_element_by_css_selector("[name = 'firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[placeholder='Enter last name']")
    input2.send_keys("Dorn")
    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys("ads.@dwd")
    input4_send_file = browser.find_element_by_css_selector("[type='file']")
    input4_send_file.send_keys(file_path)
    input5 = browser.find_element_by_css_selector("[type='submit']")
    input5.click()
    time.sleep(5)
finally:
    time.sleep(5)
    browser.quit()