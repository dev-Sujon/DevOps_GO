import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome driver with detach option
options = Options()
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Load the Excel file
df = pd.read_excel('4BeatsQ1.xlsx')

longest_options = []
shortest_options = []

for keyword in df['Keyword']:
    print(f"Searching for keyword: {keyword}")
    
    # Perform Google search
    driver.get('https://www.google.com')
    
    # Wait for the search box to be present
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'q'))
    )
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)
    
    # Wait for the results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'h3'))
    )
    
    # Extract search results
    results = driver.find_elements(By.CSS_SELECTOR, 'h3')
    options = [result.text for result in results if result.text]

    if options:
        longest_option = max(options, key=len)
        shortest_option = min(options, key=len)
    else:
        longest_option = ''
        shortest_option = ''

    longest_options.append(longest_option)
    shortest_options.append(shortest_option)

    print(f"Longest option: {longest_option}")
    print(f"Shortest option: {shortest_option}")

# Close the driver (optional, remove this line if you want to keep the browser open)
# driver.quit()

# Write results back to Excel
df['Longest Option'] = longest_options
df['Shortest Option'] = shortest_options
df.to_excel('updated_file.xlsx', index=False)
