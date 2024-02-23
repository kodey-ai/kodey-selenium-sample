from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class Driver:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--window-size=1920,1200")
        self.service = Service(ChromeDriverManager().install())
        self.driver = None

    def get_driver(self):
        if self.driver is None:
            self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
        return self.driver

    def close_driver(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None