# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MymoshouItem(scrapy.Item):
    gid = scrapy.Field()
    gname = scrapy.Field()
    duration_time = scrapy.Field()
    proportion1 = scrapy.Field()
    proportion2 = scrapy.Field()
    quantity = scrapy.Field()
    price_min = scrapy.Field()
    price_max = scrapy.Field()
