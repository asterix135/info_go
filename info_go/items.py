# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DirectoryPage(scrapy.Item):
    employee_name = scrapy.Field
    employee_info = scrapy.Field
    employee_id = scrapy.Field
