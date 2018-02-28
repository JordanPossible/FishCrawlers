import scrapy
from ..items import FishpixKahakuItem

class FishpixKahakuSpider(scrapy.Spider):
    name = 'fishpix'
    start_urls = [
    # 'http://fishpix.kahaku.go.jp/fishimage-e/familylist_1.html',
    # 'http://fishpix.kahaku.go.jp/fishimage-e/familylist_2.html',
    'http://fishpix.kahaku.go.jp/fishimage-e/familylist_3.html',
    ]

    def parse(self, response):
        all_fish_family_link = response.css('.familyBrowseList').xpath('a')
        for fish_family_link in all_fish_family_link:
            family_page_link = response.urljoin(fish_family_link.xpath('@href').extract_first())
            yield scrapy.Request(url=family_page_link, callback=self.parseFishFamily)

    def parseFishFamily(self, response):
        all_fish_link = response.css('.result').xpath('a/@href').extract()
        for fish_link in all_fish_link:
             yield scrapy.Request(url=response.urljoin(fish_link), callback=self.parseFish)
        nextPageLinkSelector = response.css('.headLink').xpath('a/@href').extract_first()
        if nextPageLinkSelector:
            yield scrapy.Request(url=response.urljoin(nextPageLinkSelector), callback=self.parseFishFamily)

    def parseFish(self, response):
        item = FishpixKahakuItem()
        item['family_name'] = response.xpath('//b').extract_first()
        item['taxonomy_name'] = response.xpath('//b').extract_first()
        item['images_urls'] = response.urljoin(response.xpath('//img/@src').extract_first())
        yield item

# nextPageLinkSelector = response.css('.NextLink::attr("href")')
# if nextPageLinkSelector:
#     nextPageLink = nextPageLinkSelector[0].extract()
#     yield scrapy.Request(url=response.urljoin(nextPageLink))

# import scrapy
# from ..items import PaloAltoItem
#
# class PaloAltoSpider(scrapy.Spider):
#     name = 'paloalto'
#     allowed_domains = ['killi.palo-alto.ca.us']
#     start_urls = [
#     'http://killi.palo-alto.ca.us/images/',
#     ]
#
#     # Crawl la page principale, creer l'objet item
#     # scrap le nom de l'espece et l'url de page concerne
#     # appel la fonction parseFish sur chaque page
#     def parse(self, response):
#         # item = PaloAltoItem()
#         all_fish_url = response.xpath('//div[@class="nom"]')
#         for fish in all_fish_url:
#             url = response.urljoin(fish.xpath('a/@href').extract_first())
#             # taxo = fish.xpath('a/span/text()').extract_first()
#             # item['taxonomy'] = taxo
#             # item['page_url'] = url
#             r = scrapy.Request(url=url, callback=self.parseFish)
#             # r.meta['item'] = item
#             yield r
#
#     def parseFish(self, response):
#         # item = response.meta['item']
#         # all_img_link = response.xpath('//a[not(contains(@id, "imageDivLink") or contains(@id, "imgdir") or contains(@href, "./home.html"))]/@href').extract()
#         all_but_menu = response.xpath('//div[not(contains(@id, "mainmenu"))]')
#         all_img_link = all_but_menu.xpath('//a/@href').extract()
#         for img_link in all_img_link:
#             r = scrapy.Request(url=response.urljoin(img_link), callback=self.parseFishPic)
#             # r.meta['item'] = item
#             yield r
#
#     def parseFishPic(self, response):
#         # item = response.meta['item']
#         lg_imgs_links = response.xpath('//a[contains(text(), "lg")]/@href').extract()
#         for lg_img_link in lg_imgs_links:
#             r = scrapy.Request(url=response.urljoin(lg_img_link), callback=self.parseFishLgPic)
#             # r.meta['item'] = item
#             yield r
#
#     def parseFishLgPic(self, response):
#         item = PaloAltoItem()
#         img_url = response.xpath('//div[@align="center"]/img/@src').extract_first()
#         # item = response.meta['item']
#         item['images_urls'] = response.urljoin(img_url)
#         yield item
