# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from urllib.parse import urlencode
import json
from images360.items import Images360Item


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']

    def start_requests(self):
        data = {'ch':'photography','listtype':'new'}
        baseurl = 'https://image.so.com/zj?'
        for page in range(1,self.settings.get('MAX_PAGE')+1):
            data['sn'] = page * 30
            params = urlencode(data)
            url = baseurl + params
            yield Request(url=url,callback=self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        for image in result.get('list'):
            item = Images360Item()
            item['url'] = image.get('qhimg_url')
            item['id'] = image.get('imageid')
            item['title'] = image.get('group_title')
            item['thumb'] = image.get('qhimg_thumb_url')
            yield item

