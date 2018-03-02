import scrapy
from ..items import PaloAltoItem

class PaloAltoSpider(scrapy.Spider):
    name = 'paloalto'
    allowed_domains = ['killi.palo-alto.ca.us']
    start_urls = [
    'http://killi.palo-alto.ca.us/images/',
    ]

    # Crawl la page principale, creer l'objet item
    # scrap le nom de l'espece et l'url de page concerne
    # appel la fonction parseFish sur chaque page
    def parse(self, response):

        all_fish_url = response.xpath('//div[@class="nom"]')
        for fish in all_fish_url:
            url = response.urljoin(fish.xpath('a/@href').extract_first())
            taxo = fish.xpath('a/span/text()').extract_first()
            item = PaloAltoItem()
            if taxo is not None:
                item['fish_url'] = url
                item['taxonomy'] = taxo
                r = scrapy.Request(url=url, callback=self.parseFish)
                r.meta['item'] = item
                yield r

    def parseFish(self, response):
        item = response.meta['item']
        # all_img_link = response.xpath('//a[not(contains(@id, "imageDivLink") or contains(@id, "imgdir") or contains(@href, "./home.html"))]/@href').extract()
        all_but_menu = response.xpath('//div[not(contains(@id, "mainmenu"))]')
        all_img_link = all_but_menu.xpath('//a/@href').extract()
        for img_link in all_img_link:
            r = scrapy.Request(url=response.urljoin(img_link), callback=self.parseFishPic)
            r.meta['item'] = item
            yield r

    def parseFishPic(self, response):
        item = response.meta['item']
        lg_imgs_links = response.xpath('//a[contains(text(), "lg")]/@href').extract()
        for lg_img_link in lg_imgs_links:
            r = scrapy.Request(url=response.urljoin(lg_img_link), callback=self.parseFishLgPic)
            r.meta['item'] = item
            yield r

    def parseFishLgPic(self, response):
        #item = PaloAltoItem()
        item = response.meta['item']
        img_url = response.xpath('//div[@align="center"]/img/@src').extract_first()
        # item = response.meta['item']
        item['image_urls'] = [response.urljoin(img_url)]
        yield item
