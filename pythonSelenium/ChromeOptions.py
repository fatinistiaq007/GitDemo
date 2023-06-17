from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("headless")
options.add_argument("--ignore-certificate-errors")

options.add_experimental_option("detach", True)
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(2)
# driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

print(driver.title)
driver.close()