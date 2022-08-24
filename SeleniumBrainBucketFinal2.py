from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

driver = webdriver.Chrome()
driver.get("https://chykalophia.com")

#verify footer (Privacy Policy/Cookie Policy)
#Privacy Policy button
PrivacyPolicy_btn = driver.find_element("xpath", "/html//div[3]/section[2]/div//div/div[3]/div/p/a[1]")
PrivacyPolicy_btn.click()
#driver.close()

driver.get('https://chykalophia.com')

driver.maximize_window()
#Cookie Policy button
CookiePolicy_btn = driver.find_element("xpath", "/html//div[3]/section[2]/div//div/div[3]/div/p/a[2]")
CookiePolicy_btn.click()
#driver.close()