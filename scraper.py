from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
import shutil
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


url = 'https://boe.cuyahogacounty.gov/candidates/campaign-finance-reports/Index'


#set up Selenium driver to manipulate Chrome browser
options=webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r".\files"
  })
browser = webdriver.Chrome(options=options)
browser.get(url)
html_source = browser.page_source

#print(html_source)

#get search input textarea
#input judge name
#click submit button
search_input = browser.find_element(By.CSS_SELECTOR, ".input-row textarea")
search_input.send_keys("Brendan Sheehan")
search_button = browser.find_element(By.CSS_SELECTOR, ".input-row div button").click()

#download files that return from search result
files = browser.find_elements(By.CSS_SELECTOR, ".table-striped tbody tr td input")
for file in files:
    print(file)
    file.location_once_scrolled_into_view
    file.click()