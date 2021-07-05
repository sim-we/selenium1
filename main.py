from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--incognito')

browser = webdriver.Chrome('./chromedriver', options=chrome_options)
browser.get('https://address')
time.sleep(5)

territoryDropDown = browser.find_element_by_id('territoryDropDown')
territoryDropDown.click()
territoryQty = browser.find_elements_by_xpath("//ul[@aria-labelledby='territoryLabel']/li")
territoryDropDown.send_keys(Keys.ESCAPE)

for i in range(len(territoryQty)):
    time.sleep(1)
    territoryDropDown.click()
    territory = browser.find_element_by_xpath(f"//ul[@aria-labelledby='territoryLabel']/li[{i+1}]")

    time.sleep(0.5)
    print (territory.text)
    territory.click()

    time.sleep(1)
    districtDropDown = browser.find_element_by_id('districtDropDown')
    districtDropDown.click()
    districtQty = browser.find_elements_by_xpath("//ul[@aria-labelledby='districtLabel']/li")
    districtDropDown.send_keys(Keys.ESCAPE)

    for i in range(len(districtQty)):
        time.sleep(1)
        districtDropDown.click()
        district = browser.find_element_by_xpath(f"//ul[@aria-labelledby='districtLabel']/li[{i+1}]")

        time.sleep(0.5)
        print (district.text)
        district.click()
        
        time.sleep(1.5)
        branchList = browser.find_elements_by_xpath("//body/main[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li")

        for branch in branchList:
            print (branch.text, '\n')
