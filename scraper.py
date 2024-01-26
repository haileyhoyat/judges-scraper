from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import csv

#function to download the files for a specific judge
def download_judge_files(name):
  
  #cuyahoga judges finance records website
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

  #get search input textarea
  #input judge name
  #click submit button
  search_input = browser.find_element(By.CSS_SELECTOR, ".input-row textarea")
  search_input.send_keys(name)
  browser.find_element(By.CSS_SELECTOR, ".input-row div button").click()

  #array of files that return from search result
  files = browser.find_elements(By.CSS_SELECTOR, ".btn-primary-outline")

  #download files from files[]
  browser.execute_script("window.scrollTo(0, 35)")
  for file in files:
      #get the file text and file id
      file_name = file.get_attribute("value")
      file_id = file.get_attribute("id")
      
      #append file text and file id to csv file
      with open('file.csv', "a", newline='') as csvfile:
          writer = csv.writer(csvfile)
          writer.writerow([file_name, file_id])
      
      # scroll down page a bit so the next file in the results is within page view
      browser.execute_script("window.scrollBy(0, 45)")
      time.sleep(.5)
      #file.click()

  browser.quit()

if __name__ == '__main__':
  download_judge_files("Andrew Santoli")
  # download_judge_files("Brendan Sheehan")
  # judges_file = open('judges.csv')
  # csvreader = csv.reader(judges_file)
  # rows = []
  # for row in csvreader:
  #   judge_name = row[1] + " " + row[2]
  #   download_judge_files(judge_name)
     