from scrapers.quotes_to_scrape import QuotesScraper

def main():
    scraper = QuotesScraper()
    scraper.scrape_quotes()
    scraper.save_quotes()
    print("Quotes scraping completed and saved to quotes_data.json")

if __name__ == "__main__":
    main()