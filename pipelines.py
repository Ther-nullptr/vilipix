# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.http.request import Request
from scrapy.pipelines.images import ImagesPipeline
from datetime import datetime, date, timedelta


class VilipixPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        data_path = (date.today() + timedelta(days = -1)).strftime("%Y%m%d")
        url = request.url
        file_name_base = url.split('/')[-1]
        file_name = file_name_base.split('_')[0]+'.jpg'
        full_url = data_path+'//'+file_name
        return full_url
    
    def item_completed(self, results, item, info):
        return item

    def get_media_requests(self, item, info):
        yield Request(item['url'])