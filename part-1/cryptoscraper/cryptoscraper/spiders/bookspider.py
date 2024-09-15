import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["bscscan.com"]
    start_urls = ["https://bscscan.com/accounts"]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'ROBOTSTXT_OBEY': False,
        'REDIRECT_ENABLED': True,
        'REDIRECT_MAX_TIMES': 5
    }

    def parse(self, response):
        links = response.css('a.me-1::attr(href)').getall()
        
        for link in links:
            yield {'link': link}
