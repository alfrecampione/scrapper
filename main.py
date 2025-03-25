from selenium import webdriver
from game_level.game import scrape_links
import pyperclip

driver = webdriver.Edge()
url = input("Enter the base URL: ")
if not url:
    exit()
parts = scrape_links(url, driver)
print(parts)

# Copy the array of links to the clipboard
pyperclip.copy("\n".join(parts))
print("Links copied to clipboard!")
