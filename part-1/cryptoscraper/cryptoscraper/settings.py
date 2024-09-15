# Scrapy settings for cryptoscraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "cryptoscraper"

SPIDER_MODULES = ["cryptoscraper.spiders"]
NEWSPIDER_MODULE = "cryptoscraper.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "cryptoscraper (+http://www.yourdomain.com)"

# Obey robots.txt rules (disable to crawl all links)
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 1  # Adjust this based on server load

# Enable AutoThrottle to manage request rate automatically
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 2  # Delay before requests are throttled
AUTOTHROTTLE_MAX_DELAY = 10  # Max delay in case of high latencies
AUTOTHROTTLE_TARGET_CONCURRENCY = 3.0  # Average number of requests Scrapy should be sending in parallel
AUTOTHROTTLE_DEBUG = False  # Set to True to see throttling stats in logs

# Enable cookies (disabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# SPIDER_MIDDLEWARES = {
#    "cryptoscraper.middlewares.CryptoscraperSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# DOWNLOADER_MIDDLEWARES = {
#    "cryptoscraper.middlewares.CryptoscraperDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# ITEM_PIPELINES = {
#    "cryptoscraper.pipelines.CryptoscraperPipeline": 300,
# }

# Set download timeout to avoid hanging requests
DOWNLOAD_TIMEOUT = 180  # 3 minutes

# Handle 302 redirects
REDIRECT_ENABLED = True

# Enable and configure HTTP caching (disabled by default)
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0  # No expiration for cache
HTTPCACHE_DIR = "httpcache"
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Prevent filtering out duplicate URLs
DUPEFILTER_CLASS = 'scrapy.dupefilters.RFPDupeFilter'

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
