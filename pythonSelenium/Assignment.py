from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.XPATH, "//a[@class='blinkingText']").click()
window_name = driver.window_handles
driver.switch_to.window(window_name[1])
full_text = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
split_text = full_text.split(" ")
i = 0
for i in range(len(split_text)):
    if "mentor@rahulshettyacademy.com" == split_text[i]:
        desired_text = split_text[i]
        break
    i += 1
driver.close()
driver.switch_to.window(window_name[0])
driver.find_element(By.ID, "username").send_keys(desired_text)
driver.find_element(By.ID, "password").send_keys("learning")
driver.find_element(By.ID, "signInBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
error = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
print(error)
driver.close()

