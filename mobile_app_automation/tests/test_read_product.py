import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.driver_setup import get_driver

@pytest.fixture(scope="module")
def setup():
    driver = get_driver()
    driver.get("http://yourapplicationurl.com")
    yield driver
    driver.quit()

def test_read_product_valid(setup):
    driver = setup
    driver.find_element(By.ID, "product-id").send_keys("1")
    driver.find_element(By.ID, "search").click()
    assert "Product details" in driver.page_source

# Add more test cases for read operation
