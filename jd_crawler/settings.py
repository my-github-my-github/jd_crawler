# -*- coding: utf-8 -*-

# Scrapy settings for jd_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jd_crawler'

SPIDER_MODULES = ['jd_crawler.spiders']
NEWSPIDER_MODULE = 'jd_crawler.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jd_crawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': '__jdu=1558431211981863967856; shshshfpa=fe7ad9f6-8a2b-9bde-b871-a843ef694fea-1558431212; shshshfpb=wu55OpVk7CHpNWz2JvBi0QA%3D%3D; __jdv=122270672|direct|-|none|-|1563782010105; areaId=28; ipLoc-djd=28-2525-2526-0; PCSYCityID=CN_620000_621000_621002; user-key=192c8767-e156-45a4-ad16-27349d4f26e8; cn=0; TrackID=1B2I0waD09qMKYHVaFgeYoXdA0gQqs8U5nYvTgx4YqaT6ogsKmlFHbg8u5y71k6kV_yOBKpA1jK_ybkXrOHYP9MtftupxjAcHiIbqmx6vEs8; pinId=q9Z9AHejG_mdmz-dTldjKLV9-x-f3wj7; pin=jd_4eacd1aef3d16; unick=jd_4eacd1aef3d16; ceshi3.com=000; _tp=wafLgunKPHIomJUDf3xl8qz5QwaZ97mUW6TS8M7ExmI%3D; _pst=jd_4eacd1aef3d16; xtest=4879.cf6b6759; __jda=122270672.1558431211981863967856.1558431212.1563782010.1564581216.4; __jdc=122270672; qrsc=1; rkv=V0900; 3AB9D23F7A4B3C9B=BMPDLMJLGCY3PVYR7HBGFPHWAMYDLVEUQEFEUCO3V7IF5PHG52VBN2YBOWNTG5LTIT3OIHM66T4EBZ6XMPRHTNEEQA; shshshfp=be60ab2067a896d1524c426baab7eb22; shshshsID=ae97032b8f57a95c7ed8941345c42506_6_1564581407883; __jdb=122270672.8.1558431211981863967856|4.1564581216; thor=33125DD2785F004993E66F57E74EEA13BA455BF474FE6B6273BEF6B9B38140823FD5E4D95063D8D0FFE42DF8C54EC0C93C16CDE82E126AE86E0ABA252F66D4367D2A383E1BFAAF9FE6724B1F333ADC6E2A28A37D9B52CE7A11C768091811BAE1B8DF801F05DF559730CA17CD4D059ABCA216178B32C657A0B4D02C2015F0A1276D8A1967B3E7089318C111BAB2641CE9E343ED5EF349639A4638DDD6D15ADA07',
    'pragma': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jd_crawler.middlewares.JdCrawlerSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'jd_crawler.middlewares.JdCrawlerDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'jd_crawler.pipelines.JdCrawlerPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
