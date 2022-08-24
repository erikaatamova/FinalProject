from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

driver = webdriver.Chrome()
driver.get("https://chykalophia.com")

#verify footer (social media)
#Linkedin button
linkedin_btn = driver.find_element("xpath", "/html//div[3]/section[2]/div/div/div/div[4]/div/div/span[1]/a/i")
linkedin_btn.click()

p = driver.current_window_handle
parent = driver.window_handles[0]
chld = driver.window_handles[1]

#switch to browser tab
driver.switch_to.window(chld)
print("Page title for browser tab:")
print(driver.title)
driver.close()
driver.switch_to.window(parent)
print("Page title for parent window")
print(driver.title)

#facebook button
facebook_btn = driver.find_element("xpath", "//*[@class='fab fa-facebook-f']")
facebook_btn.click()

p = driver.current_window_handle
parent = driver.window_handles[0]
chld = driver.window_handles[1]

#switch to browser tab
driver.switch_to.window(chld)
print("Page title for browser tab:")
print(driver.title)
driver.close()
driver.switch_to.window(parent)
print("Page title for parent window")
print(driver.title)

#twitter button
twitter_btn = driver.find_element("xpath", "/html//div[3]/section[2]//div//div[4]//div/span[3]/a/i")
twitter_btn.click()

p = driver.current_window_handle
parent = driver.window_handles[0]
chld = driver.window_handles[1]

#switch to browser tab
driver.switch_to.window(chld)
print("Page title for browser tab:")
print(driver.title)
driver.close()
driver.switch_to.window(parent)
print("Page title for parent window")
print(driver.title)

#instagram button
instagram_btn = driver.find_element("xpath", "/html//div[3]/section[2]//div//div[4]//div/span[4]/a/i")
instagram_btn.click()

p = driver.current_window_handle
parent = driver.window_handles[0]
chld = driver.window_handles[1]

#switch to browser tab
driver.switch_to.window(chld)
print("Page title for browser tab:")
print(driver.title)
driver.close()
driver.switch_to.window(parent)
print("Page title for parent window")
print(driver.title)

#youtube button
youtube_btn = driver.find_element("xpath", "/html//div[3]/section[2]//div//div[4]//div/span[5]/a/i")
youtube_btn.click()

p = driver.current_window_handle
parent = driver.window_handles[0]
chld = driver.window_handles[1]

#switch to browser tab
driver.switch_to.window(chld)
print("Page title for browser tab:")
print(driver.title)
driver.close()
driver.switch_to.window(parent)
print("Page title for parent window")
print(driver.title)

#github button
github_btn = driver.find_element("xpath", "/html//div[3]/section[2]//div//div[4]/div/div/span[6]/a/i")
github_btn.click()

p = driver.current_window_handle
parent = driver.window_handles[0]
chld = driver.window_handles[1]

#switch to browser tab
driver.switch_to.window(chld)
print("Page title for browser tab:")
print(driver.title)
driver.close()
driver.switch_to.window(parent)
print("Page title for parent window")
print(driver.title)

#behance button
behance_btn = driver.find_element("xpath", "/html//div[3]/section[2]//div//div[4]//div/span[7]/a/i")
behance_btn.click()

p = driver.current_window_handle
parent = driver.window_handles[0]
chld = driver.window_handles[1]

#switch to browser tab
driver.switch_to.window(chld)
print("Page title for browser tab:")
print(driver.title)
driver.close()
driver.switch_to.window(parent)
print("Page title for parent window")
print(driver.title)