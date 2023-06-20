from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

url="https://nidhi.tourism.gov.in/home/directory?categoryCode=01&category_name=Accommodation%20Unit"

driver = webdriver.Chrome()

driver.get(url)
df = pd.DataFrame(columns=["Name","Address","State","Princode","Category","Email","Phone number"])

list_section = driver.find_element(By.CLASS_NAME,"listing_section")
list_blocks = list_section.find_elements(By.CLASS_NAME, "listing-block")

for element in list_blocks:
    name = element.find_element(By.CLASS_NAME,"hotel-heading").get_attribute('innerHTML').strip()
    address = element.find_element(By.CLASS_NAME,"address").get_attribute('innerHTML').strip()
    address_line_1 = (address.split("\n")[-3])
    state = str(address.split("\n")[-2])
    princode =str(address.split("\n")[-1])
    #category = element.find_element(By.CLASS_NAME,"share-location").text
    #email = element.find_element(By.CLASS_NAME, "mail-details").get_attribute('innerHTML').strip()
    #phone = element.find_element(By.CLASS_NAME, "mail-details").get_attribute('innerHTML').strip()
    #contact = element.find_element(By.CLASS_NAME, "contact-details").get_attribute('innerHTML').strip()
    #df = pd.concat([])
    data = [name, address, state,princode]
    print(data)




