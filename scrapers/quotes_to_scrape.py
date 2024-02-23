import json
from selenium.webdriver.common.by import By
from driver import Driver

class QuotesScraper:
    def __init__(self):
        self.driver_instance = Driver().get_driver()
        self.quotes_page_url = "http://quotes.toscrape.com/"
        self.quotes_data = []

    def scrape_quotes(self):
        self.driver_instance.get(self.quotes_page_url)
        quotes = self.driver_instance.find_elements(By.CSS_SELECTOR, "div.quote")
        for quote in quotes:
            text = quote.find_element(By.CSS_SELECTOR, "span.text").text
            author = quote.find_element(By.CSS_SELECTOR, "span small.author").text
            tags = [tag.text for tag in quote.find_elements(By.CSS_SELECTOR, "div.tags a.tag")]
            self.quotes_data.append({"quote": text, "author": author, "tags": tags})

    def save_quotes(self):
        with open('quotes_data.json', 'w') as file:
            json.dump(self.quotes_data, file, indent=4)

    def close_scraper(self):
        self.driver_instance.quit()

if __name__ == "__main__":
    scraper = QuotesScraper()
    scraper.scrape_quotes()
    scraper.save_quotes()
    scraper.close_scraper()