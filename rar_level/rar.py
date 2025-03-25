import requests
from bs4 import BeautifulSoup
import re
import base64


def extract_url(base_url):
    try:
        response = requests.get(base_url)
        response.raise_for_status()

        # Parse the page HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract all <script> tags
        script_tags = soup.find_all("script")

        # Search for the 'download' function in the JavaScript code
        for script in script_tags:
            if script.string and "download()" in script.string:
                # Extract the line with 'window.open' in the 'download' function
                match = re.search(r'window\.open\(["\'](.*?)["\']\)', script.string)
                if match:
                    raw_url = match.group(1).strip(" \"'")

                    # Decode URL if it's encoded using atob (Base64)
                    if "atob(" in raw_url:
                        encoded_url = raw_url.split("atob(")[-1].strip(")")
                        decoded_url = base64.b64decode(encoded_url).decode("utf-8")
                        print(f"Download URL: {decoded_url}")
                        return decoded_url
                    else:
                        print(f"Download URL: {raw_url}")
                        return raw_url

        print("No download function or URL found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    while True:
        url = input("Enter the base URL: ")
        if not url:
            break
        extract_url(url)
