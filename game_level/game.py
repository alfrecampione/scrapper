from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_links(base_url, driver: webdriver.Edge):
    try:
        # Open the base URL
        driver.get(base_url)

        WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
        )

        # Extract all links
        links = [
            element.get_attribute("href")
            for element in driver.find_elements(By.TAG_NAME, "a")
            if element.get_attribute("href")
            and (
                "rar" in element.get_attribute("href")
                or "zip" in element.get_attribute("href")
            )
        ]

        # Close the browser
        driver.quit()

        return [extract_url(link) for link in links]

    except Exception as e:
        print(f"An error occurred: {e}")
        return []


from rar_level.rar import extract_url

if __name__ == "__main__":
    driver = webdriver.Edge()
    url = input("Enter the base URL: ")
    if not url:
        exit()
    parts = scrape_links(url, driver)
    print(parts)
