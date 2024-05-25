import scrapy


class KotsovolosSpider(scrapy.Spider):
    name = "kotsovolos"
    allowed_domains = ["www.kotsovolos.gr"]
    #start_urls = ["https://www.kotsovolos.gr/household-appliances/fridges/fridge-freezers"]
    custom_settings = {
            "REQUEST_FINGERPRINTER_IMPLEMENTATION": "2.7"
        }

    headers = {
        "Accept-Language":"en-US,en;q=0.8",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }

    def parse(self, response):
        yield scrapy.Request(url="https://www.kotsovolos.gr/api/ext/getProductsByCategory?params=pageNumber%3D1%26pageSize%3D36%26catalogId%3D10551%26langId%3D-24%26orderBy%3D5&catId=35822&storeId=10151&isCPage=false",
        headers = self.headers,callback=self.parse_json)

    def parse_json(self,response):
        print(response)