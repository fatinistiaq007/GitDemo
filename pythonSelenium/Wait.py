import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#Search bar
driver.find_element(By.CSS_SELECTOR, "input[class='search-keyword']").send_keys("ber")
time.sleep(2)
#Product-Name List comparison
expected_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
product_lists = driver.find_elements(By.XPATH, "//h4[@class='product-name']")
i = 0
for product_list in product_lists:
    assert expected_list[i] == product_list.text
    i += 1

items = driver.find_elements(By.XPATH, "//div[@class='products']/div")
for item in items:
    item.find_element(By.XPATH, "div/button").click()
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#Sum Validation
sum = 0
prices = driver.find_elements(By.XPATH,"//tbody/tr/td[5]/p[@class='amount']")
for price in prices:
    sum += int(price.text)
print("Sum:", sum)
total_amount = int(driver.find_element(By.CSS_SELECTOR, '.totAmt').text)
assert sum == total_amount
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)
#Total Amount > Total After Discount
total_af_discount = float(driver.find_element(By.XPATH, "//span[@class='discountAmt']").text)
print("total_af_discount: ", total_af_discount)
assert total_amount > total_af_discount

