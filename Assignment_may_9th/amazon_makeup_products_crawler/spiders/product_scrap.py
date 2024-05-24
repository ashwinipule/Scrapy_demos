import scrapy


class ProductScrapSpider(scrapy.Spider):
    name = "product_scrap"
    allowed_domains = ["www.amazon.in"]
    start_urls = ["https://www.amazon.in/gp/bestsellers/beauty/1374357031/ref=zg_bs_nav_beauty_1"]

    def parse(self, response):
        all_div_products = response.css("div.p13n-sc-uncoverable-faceout")
        #yield len(all_div_products)
        for product in all_div_products:
            product_name = product.css('div._cDEzb_p13n-sc-css-line-clamp-3_g3dy1::text').get()
            product_img_url = product.css('img::attr(src)').extract()
            ratings = product.css("span.a-icon-alt::text").get()
            yield {"product_name":product_name,
                "product_img_url":product_img_url,
                "rating":ratings
            }
