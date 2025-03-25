from selenium import webdriver
from game_level.game import scrape_links
import pyperclip

url = input("Enter the base URL: ")
print("1. edge\n2. chrome\n3. firefox")


explorer = input("Enter the browser: ")
if explorer == "1":
    driver = webdriver.Edge()
elif explorer == "2":
    driver = webdriver.Chrome()
elif explorer == "3":
    driver = webdriver.Firefox()
else:
    raise Exception("Invalid browser")

if not url:
    exit()
parts = scrape_links(url, driver)
print(parts)

# Copy the array of links to the clipboard
pyperclip.copy("\n".join(parts))
print("Links copied to clipboard!")
