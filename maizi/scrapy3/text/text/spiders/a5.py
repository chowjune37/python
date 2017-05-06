# -*- coding: utf-8 -*-
import scrapy
import json


class A5Spider(scrapy.Spider):
    name = "5"
    allowed_domains = ["120.24.68.187:8080"]
    start_urls = ['http://120.24.68.187:8080/api.php?act=showdiamonds&openid=D09AC4E940143EF6D26A627FDF9F07C5&s=10000&userid=2154&pagejsnum=1000']

    def parse(self, response):
    	r = response.body
    	a = json.loads(r)
    	print(a[1])
