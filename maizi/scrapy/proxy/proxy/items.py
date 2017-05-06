# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = scrapy.Field()
    ip = scrapy.Field()
    port = scrapy.Field()
    alpha = scrapy.Field()
    type = scrapy.Field()
    speed = scrapy.Field()
    ctime = scrapy.Field()
