import scrapy
from scrapy.http import HtmlResponse

class HhKzSpider(scrapy.Spider):
    name = 'hh_kz'
    allowed_domains = ['hh.kz']
    start_urls = ['https://hh.kz/search/vacancy?text=python&from=suggest_post&area=160']

    def parse(self, response: HtmlResponse):
        print('\n################################################################\n%s\n################################################################\n'%response.url)
