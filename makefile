# Variables
PYTHON = python
PIP = pip
REQUIREMENTS = requirements.txt
DRIVER_DIR = drivers

# Default target
all: install-requirements download-chrome-driver download-edge-driver download-firefox-driver

# Install Python requirements
install-requirements:
    $(PIP) install -r $(REQUIREMENTS)

# Download and extract the latest Chrome WebDriver
download-chrome-driver:
    mkdir -p $(DRIVER_DIR)
    curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE > $(DRIVER_DIR)/chrome_version.txt
    curl -o $(DRIVER_DIR)/chromedriver.zip https://chromedriver.storage.googleapis.com/$$(cat $(DRIVER_DIR)/chrome_version.txt)/chromedriver_win32.zip
    cd $(DRIVER_DIR) && tar -xf chromedriver.zip && del chromedriver.zip

# Download and extract the latest Edge WebDriver
download-edge-driver:
    mkdir -p $(DRIVER_DIR)
    curl -s https://msedgedriver.azureedge.net/LATEST_STABLE > $(DRIVER_DIR)/edge_version.txt
    curl -o $(DRIVER_DIR)/edgedriver.zip https://msedgedriver.azureedge.net/$$(cat $(DRIVER_DIR)/edge_version.txt)/edgedriver_win64.zip
    cd $(DRIVER_DIR) && tar -xf edgedriver.zip && del edgedriver.zip

# Download and extract the latest Firefox WebDriver
download-firefox-driver:
    mkdir -p $(DRIVER_DIR)
    curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | grep "browser_download_url.*win64.zip" | cut -d '"' -f 4 > $(DRIVER_DIR)/firefox_url.txt
    curl -o $(DRIVER_DIR)/geckodriver.zip $$(cat $(DRIVER_DIR)/firefox_url.txt)
    cd $(DRIVER_DIR) && tar -xf geckodriver.zip && del geckodriver.zip

# Set WebDriver paths in sys.path
set-sys-path:
    @echo "import sys" > set_sys_path.py
    @echo "sys.path.append('$(DRIVER_DIR)')" >> set_sys_path.py
    $(PYTHON) set_sys_path.py
    del set_sys_path.py


# Clean up drivers
clean:
    rm -rf $(DRIVER_DIR)