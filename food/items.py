# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FoodItem(scrapy.Item):

    # define the fields for your item here like:
    image              = scrapy.Field()
    imageFull         = scrapy.Field()
    ingredients        = scrapy.Field()
    unitSystem         = scrapy.Field()
    nutritionEstimates = scrapy.Field()
    keywords           = scrapy.Field()
    url                = scrapy.Field()
    name               = scrapy.Field()
    nbre_servings      = scrapy.Field()
    totalTime          = scrapy.Field()
    totalTimeInSeconds = scrapy.Field()
    rating             = scrapy.Field()
    # pass
