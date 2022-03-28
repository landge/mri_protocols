import scrapy

class ProtocolSpider(scrapy.Spider):
    name = "protocols"
    start_urls = ["https://ehandboken.ous-hf.no/folder/1334"]

    def parse(self, response):
        page =