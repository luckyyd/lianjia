# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    community = scrapy.Field()
    otherInfo = scrapy.Field()
    room = scrapy.Field()
    space = scrapy.Field()
    floor = scrapy.Field()
    direction = scrapy.Field()
    decoration = scrapy.Field()
    date = scrapy.Field()
    district = scrapy.Field()
    totalPrice = scrapy.Field()
    unitPrice = scrapy.Field()
    href = scrapy.Field()
