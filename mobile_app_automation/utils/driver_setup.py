from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver
