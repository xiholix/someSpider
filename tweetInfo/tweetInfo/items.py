# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TweetinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    tweet_num = scrapy.Field()
    fans_num = scrapy.Field()
    follow_num = scrapy.Field()
    sex = scrapy.Field()
    intro = scrapy.Field()
    means = scrapy.Field()
