from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

username = "username"
password = "password"

url = "https://saintgitsengineering.linways.com/student/"
url2 = "https://saintgitsengineering.linways.com/student/student.php?menu=online_meet&action=list"


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome("/usr/bin/chromedriver",chrome_options=options,)

driver.get(url)

driver.find_element_by_css_selector("input[type=\"text\" i]").send_keys(username)
driver.find_element_by_css_selector("input[type=\"password\" i]").send_keys(password + Keys.ENTER)

driver.get(url2)
