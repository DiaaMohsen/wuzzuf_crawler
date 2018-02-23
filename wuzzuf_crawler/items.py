# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WuzzufCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JobItem(scrapy.Item):

    	job_title = scrapy.Field()
        job_url = scrapy.Field()

        posted_on = scrapy.Field()
        job_roles = scrapy.Field()
        keywords = scrapy.Field()

        company_name = scrapy.Field()
        company_location = scrapy.Field()
        company_website = scrapy.Field()
        company_industries = scrapy.Field()


