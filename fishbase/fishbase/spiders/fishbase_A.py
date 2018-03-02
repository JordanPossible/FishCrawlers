import scrapy

from ..items import FishbaseItem

class FishbaseSpider(scrapy.Spider):
    name = 'fishbase'
    allowed_domains = ['fishbase.org']
    start_urls = [
        'http://fishbase.org/ListByLetter/ScientificNamesQ.htm'
    ]

    def parse(self, response):
        all_fish = response.xpath('//tbody/tr')
        for fish in all_fish:
            taxo = fish.xpath('td/a/i/text()').extract_first()
            fish_url = fish.xpath('td/a/@href').extract_first()

            item = FishbaseItem()
            item['taxonomy'] = taxo
            item['fish_url'] = response.urljoin(fish_url)

            r = scrapy.Request(url=response.urljoin(fish_url), callback=self.parseFish)
            r.meta['item'] = item
            yield r

    def parseFish(self, response):
        item = response.meta['item']
        imgUrl = response.xpath('//div/span/div/a/img/@src').extract_first()
        item['image_urls'] = [response.urljoin(imgUrl)]
        yield item
        # img_urls = response.urljoin(imgUrl)
        # yield img_urls

# import scrapy
# from ..items import OceanlightItem
#
# class OceanlightSpider(scrapy.Spider):
#     name = 'oceanlight'
#     allowed_domains = ['oceanlight.com']
#     start_urls = [
#     'http://www.oceanlight.com/fish.html',
#     ]
#
#     def parse(self, response):
#
#         taxo = response.xpath('//tr/td/a/i/text()').extract()
#         imageURL = response.xpath('//tr/td/a/img/@src').extract()
#
#         for item in zip(taxo, imageURL):
#             scraped_info = {
#                 'taxo' :item[0],
#                 'image_urls' :[item[1]],
#             }
#
#             yield scraped_info




# -*- coding: utf-8 -*-
# import scrapy
# from ..items import ProductItem
#
# # https://www.youtube.com/watch?v=4I6Xg6Y17qs
# scrapy crawl sportsdirect --set FEED_URI=products.json

# class SportsdirectSpider(scrapy.Spider):
#     name = 'sportsdirect'
#     allowed_domains = ['sportsdirect.com']
#     start_urls = [
#     # 'http://www.sportsdirect.com/mens/mens-rugby-boots',
#     'http://www.sportsdirect.com/mens/mens-shirts'
#     ]
#
#     def parse(self, response):
#         products = response.css('.s-productthumbbox')
#         for p in products:
#             brand = p.css('.productdescriptionbrand::text').extract_first()
#             productName = p.css('.productdescriptionname::text').extract_first()
#             price = p.css('.curprice::text').extract_first()
#             productUrl = p.css('a::attr(href)').extract_first()
#             item = ProductItem()
#             item['brand'] = brand
#             item['name'] = productName
#             item['price'] = price
#             item['url'] = response.urljoin(productUrl)
#             r = scrapy.Request(url=response.urljoin(productUrl), callback=self.parseProduct)
#             r.meta['item'] = item
#             yield r
#         nextPageLinkSelector = response.css('.NextLink::attr("href")')
#         if nextPageLinkSelector:
#             nextPageLink = nextPageLinkSelector[0].extract()
#             yield scrapy.Request(url=response.urljoin(nextPageLink))
#
#     def parseProduct(self, response):
#         item = response.meta['item']
#         imageUrls = response.css('a::attr(srczoom)').extract()
#         item['image_urls'] = imageUrls
#         yield item
