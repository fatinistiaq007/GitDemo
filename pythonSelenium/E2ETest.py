import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice")

driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()
elements = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for ele in elements:
    if ele.find_element(By.XPATH, "div/h4/a").text == "Blackberry":
        ele.find_element(By.XPATH, "div/button").click()
driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("Bangla")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[class='suggestions'] ul li a")))
driver.find_element(By.CSS_SELECTOR, "div[class='suggestions'] ul li a").click()
driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
success = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
assert "Success! Thank you!" in success
driver.close()

