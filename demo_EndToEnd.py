import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\styrt\OneDrive\Desktop\LEARNING\Selenium\chromedriver_win32\chromedriver.exe")
ch_options = Options()
ch_options.add_experimental_option("detach", True)
#ch_options.add_argument("headless") # we want to use head mode for now while building our tests.
driver = webdriver.Chrome(service=service_obj, options=ch_options)
driver.implicitly_wait(5)

def launch_browser(driver):
    #driver.get("https://thesportstak.com/")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    #driver.get("https://rahulshettyacademy.com/client/")
    #driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
    #driver.get("https://rahulshettyacademy.com/AutomationPractice")
    #driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    #driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    #driver.get("https://the-internet.herokuapp.com/iframe")
    #driver.maximize_window()
    print("testGIT")

launch_browser(driver)

driver.find_element(By.XPATH, "//a[contains(@href, 'shop')]").click() #it works
#driver.find_element(By.XPATH, "//a[text() = 'Shop']").click() #works as always
# driver.find_element(By.CSS_SELECTOR, 'a[href *="shop"]').click() # works - just tried CSS selector to be in touch.
products = driver.find_elements(By.XPATH, "//div[@class = 'card h-100']")
for i in products:
    if i.find_element(By.XPATH, "div/h4/a").text == "Blackberry":
        i.find_element(By.XPATH, "div/button").click()

#driver.find_element(By.XPATH, "//a[@class = 'nav-link btn btn-primary']").click() 1 way
driver.find_element(By.XPATH, "//a[contains(@class , 'btn')]").click() #2nd way but when using "nav-link", not working.
#driver.find_element(By.CSS_SELECTOR, "a[class *= 'btn']").click() #3rd way, see "," is needed in XPATH syntax, remember.

driver.find_element(By.XPATH, "//button[@class = 'btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
suggestions = driver.find_elements(By.XPATH, "//div[@class = 'suggestions']")

for i in suggestions:
    if i.find_element(By.XPATH, "ul/li/a").text == "India":
        i.find_element(By.XPATH, "ul/li/a").click()

driver.find_element(By.XPATH, "//label[@for = 'checkbox2']").click()
driver.find_element(By.CSS_SELECTOR, "input[value = 'Purchase']").click() # using css just for fun and rememberence.
msg = driver.find_element(By.XPATH, "//div[@class = 'alert alert-success alert-dismissible']").text

assert 'Success! Thank you!' in msg
driver.close()

