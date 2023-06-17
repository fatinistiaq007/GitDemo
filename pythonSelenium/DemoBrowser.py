from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
#Name
driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys("Fatin")
#Email
driver.find_element(By.NAME, "email").send_keys("ABC@gmail.com")
#Password
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12233dffff")
#Checkbox
driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()
#Gender
gender = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
gender.select_by_visible_text("Female")
#Employment Status
driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()
#Submit-button
driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()
msg = driver.find_element(By.CLASS_NAME, "alert-success").text
print(msg)
assert "Success!" in msg

#Two-way data binding text-box
driver.find_element(By.CSS_SELECTOR,"input.ng-dirty").send_keys("ZZZ")


