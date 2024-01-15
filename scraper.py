from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


url = 'https://boe.cuyahogacounty.gov/candidates/campaign-finance-reports/Index'


#set up Selenium driver to manipulate Chrome browser
options=webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r".\files"
  })
options.add_argument("--start-maximized")
browser = webdriver.Chrome(options=options)
browser.get(url)
html_source = browser.page_source

#print(html_source)

#get search input textarea
#input judge name
#click submit button
search_input = browser.find_element(By.CSS_SELECTOR, ".input-row textarea")
search_input.send_keys("Hollie Gallagher")
search_button = browser.find_element(By.CSS_SELECTOR, ".input-row div button").click()

#array of files that return from search result
files = browser.find_elements(By.CSS_SELECTOR, ".table-striped tbody tr td input")

#download files from files[]
browser.execute_script("window.scrollTo(0, 35)")
for file in files:
    x = file.location.get('x')
    y = file.location.get('y')
    print(y)
    # scroll down page a bit so the next file in the results is within page view
    browser.execute_script("window.scrollBy(0, 45)")
    time.sleep(.5)
    file.click()