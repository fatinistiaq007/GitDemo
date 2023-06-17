import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
# action.move_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover")).perform()
#action.context_click(driver.find_element(By.XPATH, "//a[normalize-space()='Top']")).perform()
# action.move_to_element(driver.find_element(By.XPATH, "//a[normalize-space()='Reload']")).click().perform()

#Double Click
# action.double_click(driver.find_element(By.XPATH,"//input[@id='checkBoxOption1']")).perform()

#Alert Window
# driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
# alert = driver.switch_to.alert
# alert.accept()
driver.find_element(By.XPATH, "//input[@id='confirmbtn']").click()
alert = driver.switch_to.alert
alert.dismiss()
