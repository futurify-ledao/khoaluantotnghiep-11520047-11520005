# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Demod3JsItem(scrapy.Item):
    name = scrapy.Field()
    region = scrapy.Field()
    income = scrapy.Field()
    population = scrapy.Field()
    lifeExpectancy = scrapy.Field()
    pass
