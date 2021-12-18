from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

KEY = 'YOUR_KEY'


options = webdriver.ChromeOptions()
options.add_extension('anticaptcha.crx')
driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)
driver.get('chrome-extension://lncaoejhfdpcafpkkcddpjnhnodcajfg/options.html')
# Điền key
WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="account_key_title"]')))
driver.find_elements_by_css_selector('input[name="account_key"]')[0].send_keys(KEY)

# Submit
WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"]')))
driver.find_elements_by_css_selector('input[type="submit"]')[0].click()