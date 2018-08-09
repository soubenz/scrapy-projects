
import sys
reload(sys)

import os
import re
import json
# import urllib
import scrapy

from scrapy.http import Request
from scrapy.shell import inspect_response
from food.items import FoodItem
class FoodSpider(scrapy.Spider):
    sys.setdefaultencoding('utf8')
    name = "food"
    headers = {
	'Accept': 'application/json, text/plain, */*',
	'Cache-Control': 'public, no-store',

	'Referer': 'https://www.yummly.com/',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
	'X-Yummly-Locale': 'en-US',
	'X-Yummly-Type': 'Yummly.com',
            }

    def __init__(self,maxRecipes= 2000 ,*args, **kwargs):
        super(FoodSpider, self).__init__(*args, **kwargs)
        self.max_recipes = maxRecipes

    def start_requests(self):
        l = [x for x in xrange(36,self.max_recipes,36)]
        for limit in l :
            url ='https://mapi.yummly.com/mapi/v16/content/search?maxResult=36&start={}&solr.view_type=search_internal&gs=wzl2lz&guided-search=true&startEmailLogin=true&fetchUserCollections=false&q=&allowedContent[]=single_recipe&solr.seo_boost=new&showRegistrationModal=tru'.format(
            limit)
            yield Request(url,self.parse, headers=self.headers)


    def parse(self,response):
        js = json.loads(response.body)
        for recipe in js['feed']:
            if recipe['type'] == "single recipe":

                data = recipe['content']

                try:
                    image = data['details']['images'][0]['resizableImageUrl']
                except :
                    image = None


                image_full = data['details']['images'][0]['hostedLargeUrl']
                try:
                    ingredients = data['ingredientLines']

                except :
                    self.logger.info('no ingredients')

                try :
                    unitSystem = data['imperial']
                except :
                    unitSystem = data['unitSystem']
                    pass

                try:
                    nutrition_estimates = data['nutrition']['nutritionEstimates']

                except:
                    self.logger.info('no nutrition Estimates')

                try :
                    tags = data['tags']

                except:
                    self.logger.info('no tags')

                if "keywords" in data['details']:
                    keywords = data['details']['keywords']
                else :
                    self.logger.info('no keywords')


                url = data['details']['directionsUrl']
                name =data['details']['name']
                nbre_servings = data['details']['numberOfServings']
                total_time = data['details']['totalTime']
                total_time_s = data['details']['totalTimeInSeconds']
                rating = data['details']['rating']


                recipe = FoodItem()
                recipe['image']              =image
                recipe['imageFull']         =  image_full
                recipe['ingredients']        =ingredients
                recipe['unitSystem']         =unitSystem
                recipe['nutritionEstimates'] =nutrition_estimates
                recipe['keywords']           = keywords
                recipe['totalTimeInSeconds'] =total_time_s
                recipe['totalTime']          =total_time
                recipe['nbre_servings']      =nbre_servings
                recipe['rating']             =rating
                recipe['name']               = name
                recipe['url']                = url

                yield recipe
