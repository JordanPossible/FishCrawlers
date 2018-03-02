import scrapy

from ..items import FishbaseItem


class FishbaseSpider(scrapy.Spider):
    name = 'fishbase'
    allowed_domains = ['fishbase.org']
    # start_urls = [
    # 'http://fishbase.org/search.php',
    # ]

    start_urls = [
    'http://fishbase.org/ListByLetter/ScientificNamesA.htm',
    'http://fishbase.org/ListByLetter/ScientificNamesB.htm',
    'http://fishbase.org/ListByLetter/ScientificNamesC.htm',
    'http://fishbase.org/ListByLetter/ScientificNamesD.htm',
    'http://fishbase.org/ListByLetter/ScientificNamesE.htm',
    'http://fishbase.org/ListByLetter/ScientificNamesF.htm',
    'http://fishbase.org/ListByLetter/ScientificNamesG.htm',
    # 'http://fishbase.org/ListByLetter/ScientificNamesH.htm',
    # 'http://fishbase.org/ListByLetter/ScientificNamesI.htm',
    # 'http://fishbase.org/ListByLetter/ScientificNamesJ.htm',
    # 'http://fishbase.org/ListByLetter/ScientificNamesK.htm',
    # 'http://fishbase.org/ListByLetter/ScientificNamesL.htm',
    # 'http://fishbase.org/ListByLetter/ScientificNamesM.htm',
    # 'http://fishbase.org/ListByLetter/ScientificNamesN.htm',
    # 'http://fishbase.org/ListByLetter/ScientificNamesO.htm',
    # 'http://fishbase.org/ListByLetter/ScientificNamesP.htm',
    # 'http://fishbase.org/ListByLetter/ScientificNamesQ.htm',
    # 'http://fishbase.org/ListByLetter/ScientificNamesR.htm',
    # 'http://fishbase.org/ListByLetter/ScientificNamesS.htm',
    # 'http://fishbase.org/ListByLetter/ScientificNamesT.htm',
    # 'http://fishbase.org/ListByLetter/ScientificNamesU.htm',
    # 'http://fishbase.org/ListByLetter/ScientificNamesV.htm',
    # 'http://fishbase.org/ListByLetter/ScientificNamesW.htm',
    # 'http://fishbase.org/ListByLetter/ScientificNamesX.htm',
    # 'http://fishbase.org/ListByLetter/ScientificNamesY.htm',
    # 'http://fishbase.org/ListByLetter/ScientificNamesZ.htm',
    ]

    def parse(self, response):
        # fishby_firstletter_sciname = response.css('.sciname')
        # for letter in fishby_firstletter_sciname:
        # letter_link = letter.xpath('//p[class="marginLeft100"]a/@href/text()').extract()

        # letter_link = response.css('.marginLeft100').xpath('a/@href/text()').extract()
        # img = response.css(".art-cover-photo figure a img").xpath("@src")

        # letter_link = response.css('.marginLeft100').extract()
        # letter_link = response.css('.marginLeft100').extract()
        # all_letter_link = response.xpath('//p[@class="marginLeft100"]/a/@href').extract()
        # for letter_link in all_letter_link:
        #     print(letter_link)
        all_taxo = response.xpath('//i').extract_first()
        print(all_taxo)

            #
            # # -*- coding: utf-8 -*-
            # import scrapy
            # from ..items import ProductItem
            #
            # # https://www.youtube.com/watch?v=4I6Xg6Y17qs
            # # scrapy crawl sportsdirect --set FEED_URI=products.json
            #
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
