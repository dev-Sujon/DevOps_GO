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

def test_create_product_valid(setup):
    driver = setup
    driver.find_element(By.ID, "create-product").click()
    driver.find_element(By.ID, "product-name").send_keys("Test Product")
    driver.find_element(By.ID, "product-price").send_keys("100")
    driver.find_element(By.ID, "submit").click()
    assert "Product created successfully" in driver.page_source

# Add more test cases for create operation
