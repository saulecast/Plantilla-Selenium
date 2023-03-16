# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdrivermanager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().download_and_install()))
