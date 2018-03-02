# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PaloAltoItem(scrapy.Item):
    taxonomy = scrapy.Field()
    fish_url = scrapy.Field()
    image_urls = scrapy.Field()
