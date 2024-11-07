from selenium import webdriver
from selenium.webdriver.common.by import By
import re
# Set up the WebDriver (adjust the path to your driver)
driver = webdriver.Chrome()

# Open the webpage you want to scrape
url = 'https://www.futbin.com/17/players'  # Replace with your desired URL
driver.get(url)

# Find all anchor tags (<a>) on the page
links = driver.find_elements(By.TAG_NAME, 'a')
urls = []
# Extract and print the href attribute (URL) of each link
for link in links:
    href = link.get_attribute('href')
    if href:  # Skip links without href attribute
        urls.append(href)


player_pattern = r'\/player(?!s)(?:\/|$)'

# Match the URLs
player_urls = [url for url in urls if re.search(player_pattern, url)]
for url in player_urls:
    print(url)


page_urls = []
page_pattern = r'https:\/\/www\.futbin\.com\/\d+\/players\?page=\d+$'
page_urls = [url for url in urls if re.match(page_pattern, url)]
for url in page_urls:
    print(url)

print(len(page_urls))

# Close the WebDriver after scraping
driver.quit()