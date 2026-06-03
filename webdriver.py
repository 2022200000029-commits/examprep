from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Chrome browser
driver = webdriver.Chrome()

# Open website
driver.get("https://www.google.com")

# Maximize browser window
driver.maximize_window()

# Find Google search box using name="q"
search_box = driver.find_element(By.NAME, "q")

# Type text inside search box
search_box.send_keys("Selenium Python automation")

# Submit the search
search_box.submit()

# Wait 5 seconds
time.sleep(5)

# Close browser
driver.quit()
