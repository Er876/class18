# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义 Item 非常简单，只需要继承 scrapy.Item 类，将每个要爬取的数据声明为 scrapy.Field().下面的代码是每个课程要爬取的 4 个数据。
    name = scrapy.Field()
    description = scrapy.Field()
    type = scrapy.Field()
    students = scrapy.Field() 
