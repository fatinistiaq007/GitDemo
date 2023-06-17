import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
BrowserSortedVeggies = []

options = webdriver.ChromeOptions()

# options.add_argument("headless")
# options.add_argument("--ignore-certificate-errors")

options.add_experimental_option("detach", True)
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.CSS_SELECTOR, "th:nth-child(1)").click()
veggies = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggies:
    BrowserSortedVeggies.append(ele.text)
OrgSortedList = BrowserSortedVeggies.copy()
BrowserSortedVeggies.sort()

assert OrgSortedList == BrowserSortedVeggies
