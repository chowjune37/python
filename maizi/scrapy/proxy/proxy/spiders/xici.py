# -*- coding: utf-8 -*-
import scrapy
import re
from proxy.items import ProxyItem
import sys

class XiciSpider(scrapy.Spider):
    name = "xici"
    allowed_domains = ["xicidaili.com"]
    start_urls = ['http://www.xicidaili.com/']

    def cookie_stod(self,str):
    	ss = []
    	sd = {}
    	for s in str:
    		ss.extend(s.split(';'))
    	for s in ss:
    		s = s.strip()
    		s = s.split('=')
    		if s[0] <> 'HttpOnly':
    			sd[s[0]] = s[1]
    	return sd

    def get_cookie(self,response):
    	nc = self.cookie_stod(response.headers.getlist('set-cookie'))
    	oc = self.cookie_stod(response.request.headers.getlist('cookie'))
    	oc.update(nc)
    	return oc


    def parse(self, response):
    	cookies = self.get_cookie(response)
    	body = response.body
    	url = [response.urljoin(re.findall('href="(.*?)">国内高匿代理',body)[0])]
    	# url.extend([response.urljoin(re.findall('href="(.*?)">国内普通代理',body)[0])])
    	# url.extend([response.urljoin(re.findall('href="(.*?)">国内HTTPS代理',body)[0])])
    	# url.extend([response.urljoin(re.findall('href="(.*?)">国内HTTP代理',body)[0])])
    	for u in url:
    		print('^^^\n\n^^^1^^^\n\n^^^')
    		yield scrapy.FormRequest(u,cookies=cookies,callback=self.parse1)

    def parse1(self,response):
        reload(sys)
        sys.setdefaultencoding('utf8')
        cookies = self.get_cookie(response)
        url = response.urljoin(response.css('.next_page::attr(href)').extract()[0])
        if url:
            print('\n\n-----\n')
            print(url)
            r = response.css('#ip_list tr')
            for i in r[1:]:
                pi=ProxyItem()
                pi['ip'] = i.css('td')[1].css('::text').extract()[0]
                pi['port'] = i.css('td')[2].css('::text').extract()[0]
		pi['alpha'] = i.css('td')[4].css('::text').extract()[0]
		pi['type'] = i.css('td')[5].css('::text').extract()[0]
		pi['speed'] = i.css('td')[6].css('div::attr(title)').extract()[0]
		pi['ctime'] = i.css('td')[7].css('div::attr(title)').extract()[0]
                yield pi
        yield scrapy.FormRequest(url,cookies=cookies,callback=self.parse1)

