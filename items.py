# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapeFontaneljobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CompanyItem(scrapy.Item):
    url = scrapy.Field()
    logo_url = scrapy.Field()
    meta_data = scrapy.Field()
    name = scrapy.Field()
    short_description = scrapy.Field()
    long_description = scrapy.Field()
    address = scrapy.Field()
    postal_code = scrapy.Field()
    city = scrapy.Field()

class VacancyItem(scrapy.Item):
    title = scrapy.Field()
    short_description = scrapy.Field()
    company = scrapy.Field()
    job_type = scrapy.Field()
    date = scrapy.Field()

