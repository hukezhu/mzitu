# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MzituItem(scrapy.Item):
    # define the fields for your item here like:
    mzi_name = scrapy.Field()
    mzi_link = scrapy.Field()
    mzi_view = scrapy.Field()
    mzi_time = scrapy.Field()
    mzi_image = scrapy.Field()
    mzi_index = scrapy.Field()


