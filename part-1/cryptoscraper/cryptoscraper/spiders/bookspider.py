import scrapy
import logging

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["bscscan.com"]
    start_urls = ["https://bscscan.com/accounts/1"]  # Start with page 1

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'ROBOTSTXT_OBEY': False,
        'REDIRECT_ENABLED': True,
        'REDIRECT_MAX_TIMES': 5,
        'DUPEFILTER_DEBUG': True,
        'FEED_FORMAT': 'json',
        'FEED_URI': 'output.json',  # Save the results to 'output.json'
        'LOG_LEVEL': 'DEBUG',  # Set logging level to DEBUG
    }

    def parse(self, response):
        # Extract all account links
        links = response.css('a.me-1::attr(href)').getall()
        logging.info(f"Scraped {len(links)} links from {response.url}")

        for link in links:
            # Yield the account links
            yield {'link': link}

        # Extract the current page number from the URL
        current_page = response.url.split('/')[-1]
        if current_page.isdigit():
            current_page = int(current_page)
        else:
            current_page = 1

        # Generate the next page URL
        next_page = current_page + 1
        if next_page <= 400:  # Adjust this if there are more or fewer pages
            next_page_url = response.urljoin(f"/accounts/{next_page}")
            logging.info(f"Found next page: {next_page_url}")
            # Follow the next page link and call the parse function recursively
            yield scrapy.Request(next_page_url, callback=self.parse, dont_filter=True)
        else:
            logging.info("No more pages to scrape.")
