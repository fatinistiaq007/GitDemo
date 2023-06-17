from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

rd_btns = driver.find_elements(By.XPATH, "//input[@class='radioButton']")
print(len(rd_btns))
for rd_btn in rd_btns:
    if rd_btn.get_attribute("value") == "radio1":
        rd_btn.click()
        assert rd_btn.is_selected()
        break

