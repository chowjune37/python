# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
from demo.items import DemoItem
import re
import sys

class ImageSpider(scrapy.Spider):
    name = "image"
    allowed_domains = ["douban.com"]
    start_urls = ['https://www.douban.com/']

    def list_to_dict(self,s):
        d=[]
        for i in s:
            d.extend(i.split(";"))
        s = d
        d = {}
        for i in s:
            d.setdefault(i.split("=")[0],i.split("=")[1])
        return d
    def new_cookies(self,response):
        new = self.list_to_dict(response.headers.getlist("set-cookie"))
        old = self.list_to_dict(response.request.headers.getlist("cookie"))
        old.update(new)
        return old

    def parse(self, response):
        l_url=response.css('#lzform::attr(action)').extract()[0]
        formdata = {'source':'index_nav',
                'form_email':'chowjune37@hotmail.com',
                'form_password':'a6768247177'}
        cookies = self.new_cookies(response)
        with open('index.html','w') as f:
            f.write(response.body)
        yield scrapy.FormRequest(l_url,formdata=formdata,cookies=cookies,callback=self.login)

    def login(self,response):
        m_url='https://movie.douban.com/tag/恐怖'
        cookies = self.new_cookies(response)
        with open('index2.html','w') as f:
            f.write(response.body)
        yield scrapy.FormRequest(m_url,cookies=cookies,callback=self.movie)

    def movie(self,response):
        print('--------\n\n\n\n\n')
        cookies = self.new_cookies(response)
        n_url = response.css('.next a::attr(href)').extract()[0]
        t_p = response.css('.thispage ::text').extract()[0]
        i_url = response.css('#content div div div table tr td div a::attr(href)').extract()
        for i in i_url:
            print(i)
            yield scrapy.FormRequest(i,cookies=cookies,callback=self.idt)
        yield scrapy.FormRequest(n_url,cookies=cookies,callback=self.movie)


    def idt(self,response):
        demo = DemoItem()
        name = response.css('#content h1 span ::text').extract()[0]
        year = response.css('#content .year ::text').extract()[0]
        # r = response.css('#info').re("<span class=\"pl\">制片国家/地区:</span>(.*?)<br")
        # r = response.css('#info').re("<span class=\"pl\">[\u4e00-\u9fa5]*?/[\u4e00-\u9fa5]*?:</span>(.*?)<br")
        # r = response.css('#info').re("\<span class\=\"pl\"\>.*?\/.*?\:\<\/span\>(.*?)\<br")
        country = "" 
        for i in response.css('#info').extract():
            country = country + i
        r = re.findall("\<span class\=\"pl\"\>.*?\/.*?\:\<\/span\>(.*?)\<br",country)
        # r = re.findall("<span class=\"pl\">[\u4e00-\u9fa5]*?/[\u4e00-\u9fa5]*?:</span>(.*?)<br",country)
        # r = re.findall("<span class=\"pl\">制片国家/地区:</span>(.*?)<br",country)
        indt = ""
        for i in response.css('.related-info .indent span ::text').extract():
            indt = indt + i
        print('\n\n\n------\n\n\n')
        print(name)
        print('\n......\n')
        print(country)
        # print(r)
        print('\n......\n')
        print(r)
        print('\n\n\n------\n\n\n')
        demo['name'] = name
        demo['year'] = year
        demo['co'] = r[0]
        demo['idn'] = indt
        return demo
