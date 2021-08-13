from vilipix.items import VilipixItem
import scrapy
from scrapy import Spider, Request
from datetime import datetime, date, timedelta
from urllib.parse import urlencode
import json

IMAGES = 25 # 手动指定一天的图片数

class PixivSpider(scrapy.Spider):
    name = 'pixiv'
    allowed_domains = ['vilipix.com']
    start_urls = ['http://vilipix.com/']

    def start_requests(self):
        # 为确保可以加载图片,选取昨天的网址
        yesterday = (date.today() + timedelta(days = -1)).strftime("%Y%m%d")
        base_params = {'mode':'daily','date':yesterday,'limit':IMAGES,'offset':0}
        base_url = 'https://www.vilipix.com/api/illust?'
        params = urlencode(base_params)
        url = base_url+params
        yield Request(url,self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        for image in result.get('rows'):
            item = VilipixItem()
            item['id'] = image.get('id')
            item['url'] = image.get('regular_url')
            item['title'] = image.get('title')
            print("id:{}\t url:{}\t title:{}".format(item['id'],item['url'],item['title']))
            yield item
