from behave import given, when, then
from selenium import webdriver
from features.pages.login_page import LoginPage

@given('the user is on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://accounts.shopify.com/store-login")
    context.login_page = LoginPage(context.driver)

@when('the user enters valid credentials')
def step_impl(context):
    context.login_page.enter_username("valid_user")
    context.login_page.enter_password("valid_password")
    context.login_page.click_login()

@then('the user should be redirected to the dashboard')
def step_impl(context):
    assert "Dashboard" in context.driver.title
    context.driver.quit()

@when('the user enters invalid credentials')
def step_impl(context):
    context.login_page.enter_username("invalid_user")
    context.login_page.enter_password("invalid_password")
    context.login_page.click_login()

@then('an error message should be displayed')
def step_impl(context):
    assert "Invalid credentials" in context.driver.page_source
    context.driver.quit()
