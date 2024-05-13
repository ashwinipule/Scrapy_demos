import scrapy
from ..items import AoneplusItem


class LaptopInfoScrapeSpider(scrapy.Spider):
    name = "laptop_info_scrape"
    allowed_domains = ["aoneplus.com"]
    start_urls = ["https://aoneplus.com/product-category/computers-laptops/laptops"]

    def parse(self, response):

        items =  AoneplusItem()

        all_div_products = response.css("div.product-inner")

        for product in all_div_products:
            product_name = product.css("h2.woocommerce-loop-product__title::text").extract()
            product_img_url = product.css('img::attr(src)').extract()
            product_price = product.css("bdi::text").get()
            # yield {"product_name":product_name,
            #         "product_img_url":product_img_url,
            #         "product_price":product_price
            # }
            items['product_name']=product_name
            items['product_img_url']=product_img_url
            items['product_price']=product_price

            yield items
        next_page = response.css("li>a.next::attr(href)").extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        
