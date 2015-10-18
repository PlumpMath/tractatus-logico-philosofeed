import scrapy

class QuestionSpider(scrapy.Spider):
    name = 'questionspider'
    start_urls = ['https://www.reddit.com/r/needadvice/new']

    def parse(self, response):
        for post_title in response.css('a.title::text').extract():
            yield post_title
            
    
