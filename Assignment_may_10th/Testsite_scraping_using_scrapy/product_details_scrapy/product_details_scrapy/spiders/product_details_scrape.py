import scrapy


class ProductDetailsScrapeSpider(scrapy.Spider):
    name = "product_details_scrape"
    allowed_domains = ["webscraper.io"]
    start_urls = ["https://webscraper.io/test-sites/e-commerce/static/computers/tablets"]

    def parse(self, response):
        all_div_products = response.xpath("//div[@class='card thumbnail']")
        #yield len(all_div_products)
        for product in all_div_products:
            product_name = product.css('a.title::text').get()
            product_img_url = product.css('img::attr(src)').extract()
            product_price = product.css('h4.pull-right::text').extract()
            review = product.css("p.float-end::text").get()
            yield {"product_name":product_name,
                    "product_img_url":product_img_url,
                    "product_price":product_price,
                    "review":review
            }
        try:
            next_page = response.css('a[rel=next]').attrib['href']
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
        except:
            pass
            
