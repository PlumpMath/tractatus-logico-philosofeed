# -*- coding: utf-8 -*-
import scrapy
from unidecode import unidecode


class BuzzfeedSpider(scrapy.Spider):
    name = "buzzfeed"
    url_pattern = "http://www.buzzfeed.com/index/paging?p={0}&r=1&z=4OWXYZ"
    allowed_domains = ["buzzfeed.com"]
    start_page = 1
    number_of_pages_to_crawl = 10
    
    start_urls = []
    
    for x in zip(*[iter(range(start_page,start_page+number_of_pages_to_crawl-1))]):
        start_urls.append(url_pattern.format(*x))
    
    print start_urls
    def parse(self, response):
        for text in response.css("h2 a.lede__link::text"):
            title = unidecode(text.extract()).strip()
            # print title
            yield { 'title': title }
